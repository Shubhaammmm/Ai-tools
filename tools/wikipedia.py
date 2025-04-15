import warnings
from langchain.utilities import WikipediaAPIWrapper

# Suppress deprecation warning for WikipediaAPIWrapper
warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    message="Importing WikipediaAPIWrapper from langchain.utilities is deprecated."
)

def run(message: str, params: dict):
    """
    Executes a Wikipedia search query and retrieves the result.

    Args:
        message (str): The search query or message.
        params (dict): Additional parameters (not used for this tool but included for standardization).

    Returns:
        dict: A dictionary containing the status, results, or error message.
    """
    try:
        if not message or not message.strip():
            return {"status": "error", "message": "Message is required for Wikipedia search"}

        # Initialize WikipediaAPIWrapper
        wikipedia = WikipediaAPIWrapper()

        # Debug: Print the extracted message
        print(f"Received search query: '{message}'")

        # Perform the Wikipedia search
        result = wikipedia.run(message.strip())

        # Debug: Print the raw result
        print(f"Wikipedia search result: {result}")

        # Check if the result is empty or indicates no relevant information
        if not result or result == "No good Wikipedia Search Result was found":
            return {"status": "error", "message": "No relevant Wikipedia results found. Please refine your search."}

        # Return the successful result
        return {"status": "success", "results": result}

    except Exception as e:
        # Handle and log exceptions
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
