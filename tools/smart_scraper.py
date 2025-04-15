import os
import json
from langchain_scrapegraph.tools import SmartScraperTool

# Set the API key for SmartScraperTool
os.environ["SGAI_API_KEY"] = "sgai-e5cf46ec-125c-46c9-9a63-a912c5535789"

def run(data: dict, *args, **kwargs) -> dict:
    """
    Executes the scraping operation for the given tool and data.

    Args:
        data (dict or str): A dictionary containing the command, tool, and input parameters.
                            If a string is provided, it will be parsed as JSON.
                            Expected format:
                            {
                                "command": "run",
                                "tool": "smart_scraper",
                                "data": {
                                    "params": {
                                        "url": "https://example.com"
                                    },
                                    "message": "Extract all headings from the page"
                                }
                            }
        *args: Additional positional arguments (ignored).
        **kwargs: Additional keyword arguments (ignored).

    Returns:
        dict: The result of the scraping operation, or an error message.
    """
    try:
        # Ensure `data` is a dictionary
        if isinstance(data, str):
            try:
                data = json.loads(data)  # Convert JSON string to dictionary
            except json.JSONDecodeError:
                return {"status": "error", "message": "Invalid JSON input"}

        if not isinstance(data, dict):
            return {"status": "error", "message": "Input data must be a dictionary or valid JSON string"}

        # Extract command, tool, and inner data
        command = data.get("command", "").strip()
        tool = data.get("tool", "").strip()
        inner_data = data.get("data", {})

        if command != "run" or tool != "smart_scraper":
            return {"status": "error", "message": "Invalid command or tool"}

        # Extract URL and query from inner_data
        params = inner_data.get("params", {})
        url = params.get("url", "").strip()
        query = inner_data.get("message", "").strip()

        if not url:
            return {"status": "error", "message": "Website URL is required for scraping"}
        if not query:
            return {"status": "error", "message": "Query is required for describing what to extract"}

        # Initialize the SmartScraperTool
        smartscraper = SmartScraperTool()

        # Debug: Print the URL and query being processed
        print(f"Scraping URL: {url}")
        print(f"User Query: {query}")

        # Perform the scraping operation
        result = smartscraper.invoke({
            "user_prompt": query,
            "website_url": url,
        })

        # Debug: Print the raw result from SmartScraperTool
        print(f"SmartScraperTool Result: {result}")

        # Return the successful result
        return {"status": "success", "results": result}

    except Exception as e:
        # Handle and log exceptions
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
