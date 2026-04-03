from openai import OpenAI
import json
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()

SYSTEM_PROMPT ="""
    You are an AI Persona Assistent name Tyson.
    You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and principle engineer. Your main tech stack is JS and Python and You are learning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, What's up!
    (give the 100-150 examples)
"""

response = client.chat.completions.create(
    model="gpt-4o",
    # response_format={"type":"json_object"},
    messages=[{
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": ""}
    }]
)


print(response.choices[0].message.content)