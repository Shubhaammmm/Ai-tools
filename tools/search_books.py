import os
from langchain_community.tools.google_books import GoogleBooksQueryRun
from langchain_community.utilities.google_books import GoogleBooksAPIWrapper

# Set the environment variable for Google Books API Key
os.environ["GOOGLE_BOOKS_API_KEY"] = "AIzaSyATyX029_3h5JDzza0iT4PU3UFuJbNeMfI"

# Initialize the tool for querying Google Books
tool = GoogleBooksQueryRun(api_wrapper=GoogleBooksAPIWrapper())

def run(message: str, params: dict):
    """
    Searches for books using the Google Books API based on the provided query.

    Args:
        message (str): The query string to search books.
        params (dict): Additional parameters (not used here but kept for standardization).

    Returns:
        dict: Status and the search results or an error message.
    """
    try:
        # Run the Google Books search query
        result = tool.run(message)
        return {"status": "success", "results": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
