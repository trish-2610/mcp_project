## news server
from mcp.server.fastmcp import FastMCP
import feedparser

mcp = FastMCP("news-server")

@mcp.tool()
def get_market_news():
    """Fetch latest financial market news"""

    try:
        rss_url = "https://news.google.com/rss/search?q=stock+market&hl=en-IN&gl=IN&ceid=IN:en"
        feed = feedparser.parse(rss_url)

        news_list = []

        for entry in feed.entries[:5]:
            source = "Unknown"
            if hasattr(entry, "source"):
                source = entry.source.title
            news_list.append({
                "title": entry.title,
                "source": source,
                "link": entry.link
            })

        return news_list

    except Exception as e:
        return {
            "error": str(e)
        }

@mcp.tool()
def get_company_news(company: str):
    """Fetch company news"""

    try:

        query = company.replace(" ", "+")
        rss_url = f"https://news.google.com/rss/search?q={query}+stock&hl=en-IN&gl=IN&ceid=IN:en"
        feed = feedparser.parse(rss_url)

        news_list = []

        for entry in feed.entries[:5]:

            source = "Unknown"
            if hasattr(entry, "source"):
                source = entry.source.title
            news_list.append({
                "title": entry.title,
                "source": source,
                "link": entry.link
            })

        return news_list

    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    print("News MCP server started...")
    mcp.run()