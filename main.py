import asyncio
from supervisor.supervisor_agent import create_system


async def main():

    supervisor = await create_system()

    query = input("Ask a financial intelligence question: ")

    final_message = ""

    async for chunk in supervisor.astream(
        {"messages": [{"role": "user", "content": query}]}
    ):

        # Only capture the final supervisor response
        if "supervisor" in chunk:

            data = chunk["supervisor"]

            if data and "messages" in data:
                for m in data["messages"]:

                    if hasattr(m, "content") and m.content:
                        final_message = m.content

    print("\n====================================")
    print("FINANCIAL INTELLIGENCE REPORT")
    print("====================================")
    print(final_message)


if __name__ == "__main__":
    asyncio.run(main())