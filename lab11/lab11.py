import asyncio
import sys
from pathlib import Path

# MCP imports
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# LangChain MCP adapter
from langchain_mcp_adapters.tools import load_mcp_tools

# Updated agent import
from langchain.agents import create_agent

# Ollama LLM via LangChain
from langchain_ollama import ChatOllama


# Configuration
MCP_SERVER_SCRIPT = Path(__file__).parent / "mcp_server.py"
OLLAMA_MODEL = "llama3.2:latest"
SYSTEM_PROMPT = (
    "You are a helpful DnD assistant. "
    "Use the available tools to help players with dice rolls, character stats, and damage calculations."
)


async def chat_with_tools(user_message: str, agent) -> str:
    """
    Send a message to the agent and return the final response.
    """
    try:
        result = await agent.ainvoke({
            "messages": [{"role": "user", "content": user_message}]
        })
        return result["messages"][-1].content
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    print("=" * 60)
    print("Lab 11: MCP + LangGraph Integration")
    print("=" * 60)

    if not MCP_SERVER_SCRIPT.exists():
        print(f"\nError: MCP server not found at {MCP_SERVER_SCRIPT}")
        print("Make sure you've created mcp_server.py")
        return

    print(f"\nConnecting to MCP server: {MCP_SERVER_SCRIPT.name}")

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(MCP_SERVER_SCRIPT)]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("[OK] Connected to MCP server!")

            tools = await load_mcp_tools(session)

            print(f"\nFound {len(tools)} tools:")
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")

            if not tools:
                print("\nNo tools found! Make sure you've implemented list_tools() in mcp_server.py")
                return

            llm = ChatOllama(model=OLLAMA_MODEL)

            agent = create_agent(
                model=llm,
                tools=tools,
                system_prompt=SYSTEM_PROMPT
            )

            print("\n" + "-" * 60)
            print("Chat with the DnD assistant (type 'quit' to exit)")
            print("Try: 'Roll a d20 for an attack' or 'What is the fighter's strength?'")
            print("-" * 60 + "\n")

            while True:
                try:
                    user_input = input("You: ").strip()
                except (EOFError, KeyboardInterrupt):
                    break

                if not user_input:
                    continue

                if user_input.lower() in ["quit", "exit", "q"]:
                    print("Goodbye!")
                    break

                response = await chat_with_tools(user_input, agent)
                print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    asyncio.run(main())