import os 
from langchain_groq import ChatGroq
from langgraph_supervisor import create_supervisor
from agents.economic_agent import create_economic_agent
from agents.corporate_agent import create_corporate_agent
from agents.news_agent import create_news_agent
from dotenv import load_dotenv  
load_dotenv()

async def create_system():
    economic_agent = await create_economic_agent()
    news_agent = await create_news_agent()
    corporate_agent = await create_corporate_agent()

    model = ChatGroq(
        model = "llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    supervisor = create_supervisor(
    model=model,
    agents= [economic_agent,news_agent,corporate_agent],
    prompt="""
        You are the supervisor of a financial intelligence system.

        Agents available:
        - economic_agent → macroeconomic indicators
        - news_agent → financial news analysis
        - corporate_agent → company and industry intelligence

        Workflow:

        1. Route the user request to the most relevant agent.
        2. Wait for the agent to finish.
        3. DO NOT call the same agent again.
        4. Produce a FINAL structured report.

        IMPORTANT RULES:
        - Do NOT show tool calls.
        - Do NOT show transfer messages.
        - Only output the final analysis.

        Final output format:

        FINANCIAL INTELLIGENCE REPORT

        Summary:
        (short overall insight)

        Key Signals:
        (list important findings)

        Market Outlook:
        (Bullish / Neutral / Bearish)
        """,
    ).compile()

    return supervisor
