import os 
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from config import get_model
load_dotenv()

async def create_economic_agent():
    client = MultiServerMCPClient(
        {
            "economic_server": {
                "command" : "python",
                "args" : ["mcp_servers/economic_server.py"],
                "transport" : "stdio"
            }
        }
    )

    tools = await client.get_tools()

    economic_agent = create_agent(
        model = get_model(),
        tools = tools,
        system_prompt="""
        You are a macroeconomic intelligence analyst.

        Use the economic tools to fetch:
        - inflation
        - interest rates
        - unemployment

        Analyze how these indicators affect financial markets.

        Return your response STRICTLY in the following format:

        ECONOMIC SIGNAL REPORT

        Inflation:
        (value + short explanation)

        Interest Rate:
        (value + short explanation)

        Unemployment:
        (value + short explanation)

        Market Impact:
        (Explain overall macroeconomic sentiment: Bullish / Neutral / Bearish)
        """,
        name="economic_agent"
    )
    return economic_agent