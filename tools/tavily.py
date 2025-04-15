import os
from langchain_community.tools import TavilySearchResults

# Set the Tavily API key as an environment variable
os.environ["TAVILY_API_KEY"] = "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"

def run(message: str, params: dict):
    """
    Executes a search query using Tavily and retrieves the results.

    Args:
        message (str): The search query.
        params (dict): Additional parameters for the search (optional).

    Returns:
        dict: A dictionary containing the status, results, or error message.
    """
    try:
        if not message or not message.strip():
            return {"status": "error", "message": "Message is required for Tavily search"}

        # Configure the TavilySearchResults tool
        tools = TavilySearchResults(
            max_results=params.get("max_results", 5),
            search_depth=params.get("search_depth", "advanced"),
            include_answer=params.get("include_answer", True),
            include_raw_content=params.get("include_raw_content", True),
            include_images=params.get("include_images", True),
        )

        # Debug: Print the query and parameters
        print(f"Executing Tavily search with query: '{message}' and params: {params}")

        # Perform the search
        result = tools.invoke(message.strip())

        # Debug: Print the raw result
        print(f"Tavily search result: {result}")

        # Check if the result is empty
        if not result:
            return {"status": "error", "message": "No results found for the given query"}

        # Return the successful result
        return {"status": "success", "results": result}

    except Exception as e:
        # Handle and log exceptions
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
