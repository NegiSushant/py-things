from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools

# mcp_client = streamablehttp_client(url=mcp_server)

async def main():
    async with streamablehttp_client("http://localhost:8000/mcp/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)
    print(tools)

if __name__ =="__main__":
    asyncio.run(main())