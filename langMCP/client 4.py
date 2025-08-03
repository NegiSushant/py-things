import asyncio
import json
import re
from openai import AzureOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Azure OpenAI configuration (replace with your actual Azure credentials)
AZURE_OPENAI_ENDPOINT = ""
AZURE_OPENAI_API_KEY = ""
AZURE_OPENAI_DEPLOYMENT_NAME = ""
AZURE_OPENAI_API_VERSION = "2024-12-01-preview"

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Client initialized successfully.")
            print("""
Welcome to the MCP Demo with Azure OpenAI Support. You can:
- Manage customers (e.g., list customers, add a customer, etc.)
- Chat about anything (e.g., ask questions, say hello)
- Type "quit" to exit
            """)
            while True:
                prompt = input("Enter your query: ").strip()

                if prompt.lower() == "quit":
                    break

                response = await analyze_prompt_with_llm(prompt)
                print(f"[DEBUG] LLM response: {response}")  # Log LLM output
                if "tool" in response and response["tool"]:
                    tool = response["tool"]
                    args = response["args"]
                    print(f"[DEBUG] Calling tool: {tool} with args: {args}")
                    result = await session.call_tool(tool, args)
                    result_str = str(result)
                    print(generate_response(tool, result_str))
                elif "chat_response" in response:
                    print(response["chat_response"])
                else:
                    print("Sorry, I didn’t quite get that. Could you try again?")
                    
async def analyze_prompt_with_llm(prompt):
    """Analyze the user's query using Azure OpenAI's GPT model."""
    system_message = """
You are a helpful assistant that can either:
1. Manage a customer database with these tools:
   - add_customer(name: str, email: str): Add a new customer.
   - update_customer(id: int, name: str, email: str): Update a customer by ID.
   - delete_customer(id: int): Delete a customer by ID.
   - get_customer(id: int): Retrieve a customer by ID.
   - get_all_customers(): Retrieve all customers.

2. Respond conversationally to general questions or statements not related to the database.

Analyze the user's query and return a JSON object with ONE of these:
- For database tools: {"tool": "tool_name", "args": {"arg1": value1, ...}}
- For general chat: {"chat_response": "Your conversational response here"}
- If unclear: {"tool": null, "args": {}}

Only call a tool if the query clearly relates to customer management. Otherwise, respond naturally as a chatbot. Ensure arguments match the tool's requirements (e.g., id must be an integer).
"""

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]  
        )
        llm_output = response.choices[0].message.content.strip()

        
        json_pattern = r"```(?:json)?\s*([\s\S]*?)```"
        match = re.search(json_pattern, llm_output)
        if match:
            llm_output = match.group(1).strip()

        # Parse the LLM output
        try:
            parsed_output = json.loads(llm_output)
            return parsed_output
        except json.JSONDecodeError as e:
            print(f"Error parsing LLM output: {llm_output}")
            print(f"JSON error: {e}")
            return {"tool": None, "args": {}}
    except Exception as e:
        print(f"Error in LLM analysis: {e}")
        return {"tool": None, "args": {}}

def generate_response(tool, result):
    """Convert tool output to natural language."""
    try:
        result_data = json.loads(result)
        if tool == "get_all_customers":
            if isinstance(result_data, list) and result_data:
                customer_list = ", ".join([f"{c['name']} (ID: {c['id']})" for c in result_data])
                return f"Here’s the list of customers: {customer_list}."
            return "There aren’t any customers in the database yet."
        elif tool == "get_customer":
            if "id" in result_data:
                return f"I found the customer: {result_data['name']} with email {result_data['email']} (ID: {result_data['id']})."
            return "I couldn’t find a customer with that ID."
        elif tool == "add_customer":
            if "id" in result_data:
                return f"I’ve added {result_data['name']} with email {result_data['email']} to the database. Their ID is {result_data['id']}."
            return "Something went wrong while adding the customer."
        elif tool == "update_customer":
            if result_data.get("success"):
                return "I’ve updated the customer’s details successfully."
            return "I couldn’t find a customer with that ID to update."
        elif tool == "delete_customer":
            if result_data.get("success"):
                return "The customer has been deleted."
            return "There was no customer with that ID to delete."
        return "Hmm, I got a response from the server, but I’m not sure how to interpret it."
    except json.JSONDecodeError:
        return f"The server said: {result}. Does that make sense to you?"
    except Exception as e:
        return f"Oops, something went wrong: {str(e)}"

if __name__ == "__main__":
    asyncio.run(main())