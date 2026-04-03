from openai import OpenAI
import json
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()

SYSTEM_PROMPT ="""
    You're an expert AI Assistent in resolving user queries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to ne done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user.)

    output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT",  "Content": "string"}

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: {"step": "PLAN": "content":"looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN": "content":"Yes, The BODMAS is correct thing to be done here"}
    PLAN: {"step": "PLAN": "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN": "content": "we must perform divide that is 15 / 10"}
    PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN": "content": "Now finally lets perform the add 3.5"}
    PLAN: {"step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans"}
    PLAN: {"step": "PLAN": "content": "3.5"}
"""

message_history = [{
    "role": "system", "content": SYSTEM_PROMPT
}]

user_query = input("-->")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type":"json_object"},
        messages=message_history
    )
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistent", "content":raw_result})

    parsed_result = json.loads(raw_result)
    if parsed_result.get("step") == "START":
        print("<>", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "PLAN":
        print("<<>>", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("<<!>>", parsed_result.get("content"))
        break

# response = client.chat.completions.create(
#     model="",
#     response_format={"type":"json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content":"Hey, Write a code to add n numbers in js"},
#         # Manually keep 
#     ]
# )

print(response.choices[0].message.content)