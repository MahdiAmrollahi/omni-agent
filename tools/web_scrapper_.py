from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
import os 

@tool
def web_scrapper(url: str) -> str:
    """
    Scrape a web page and return the content.
    Args:
        url: The URL of the web page to scrape.
    Returns:
        The content of the web page.
    Example:
        web_scrapper("https://example.com/")
        Returns:
            {"url": "https://example.com/", "content": "The content of the web page."}
    """
    loader = WebBaseLoader(web_paths=[url])
    docs = loader.load()
    return {"url": url, "content": docs[0].page_content}
