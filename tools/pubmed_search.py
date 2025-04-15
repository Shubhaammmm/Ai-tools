from langchain_community.tools.pubmed.tool import PubmedQueryRun

# Initialize the PubMed query tool
tool = PubmedQueryRun()

def run(message: str, params: dict):
    """
    Executes a query on PubMed and returns the results.

    Args:
        message (str): The query string for PubMed search.
        params (dict): Additional parameters (not used here but kept for standardization).

    Returns:
        dict: Status and the search results or an error message.
    """
    try:
        # Run the PubMed query
        result = tool.invoke(message)
        return {"status": "success", "results": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
