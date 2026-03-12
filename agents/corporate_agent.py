## corporate_agent
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from config import get_model
import os 
from dotenv import load_dotenv
load_dotenv()

async def create_corporate_agent():

    client = MultiServerMCPClient(
        {
            "corporate_server" : {
                "command" : "python",
                "args" : ["mcp_servers/corporate_server.py"],
                "transport" : "stdio"       
            }
        }
    )

    tools = await client.get_tools() ## initializing tools 

    corporate_agent = create_agent( ## create corporate agent 
        model = get_model(),
        tools = tools,
        system_prompt=
        """
        You are a corporate intelligence analyst.

        Your tasks:
        - identify competitors
        - analyze industry structure
        - detect important industry trends

        Return your response in this format:

        CORPORATE INTELLIGENCE REPORT

        Company:
        (company analyzed)

        Key Competitors:
        (list competitors)

        Industry Trend:
        (short explanation)

        Competitive Impact:
        (How this affects the company's market position)

        Investment Insight:
        (Bullish / Neutral / Bearish)
        """,
        name="corporate_agent"
    )

    return corporate_agent