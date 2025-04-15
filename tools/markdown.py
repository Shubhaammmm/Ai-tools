from langchain_scrapegraph.tools import MarkdownifyTool
import os

# Set the API key for SGAI
os.environ["SGAI_API_KEY"] = "sgai-e5cf46ec-125c-46c9-9a63-a912c5535789"

def run(message: str, params: dict):
    """
    Converts the content of a given website URL into Markdown format.

    Args:
        message (str): Command or instruction (not used but included for standardization).
        params (dict): Contains 'url' to convert into Markdown.

    Returns:
        dict: A dictionary with status and Markdown result or error message.
    """
    try:
        # Accessing the URL from params
        url = params.get("url", "").strip()

        # Check if URL is provided
        if not url:
            return {"status": "error", "message": "URL is required"}

        # Initialize the MarkdownifyTool
        markdownify = MarkdownifyTool()
        
        # Invoke the tool with the website URL as input
        markdown = markdownify.invoke({"website_url": url})
        
        return {"status": "success", "message": "Markdown conversion successful", "markdown": markdown}

    except Exception as e:
        return {"status": "error", "message": f"Error: {e}"}