# backend/tools/search_tool.py

import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(query: str) -> str:
    """
    Search the web and return formatted search results.
    """

    response = client.search(
        query=query,
        search_depth='basic',
        max_results=3
    )

    results = []

    for item in response["results"]:
        results.append(
            f"""
Title: {item['title']}

Content:
{item['content']}

Source:
{item['url']}
"""
        )

    return "\n\n".join(results)