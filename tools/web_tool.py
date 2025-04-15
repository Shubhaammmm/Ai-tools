import os
from composio_langchain import ComposioToolSet

# Set API Keys

# Initialize Composio ToolSet
composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")

def run(message:str, params:dict):
    """
    Executes the tool based on provided parameters.

    Args:
        message (str): Description of the task (optional, default: "").
        params (dict): Dictionary containing:
            - "website_url" (str): Target website URL.
            - "element_selector" (str): CSS selector for scraping.

    Returns:
        dict: Scraped data or an error message.
    """
    try:
        if params is None:
            return {"status": "error", "message": "Parameters cannot be empty"}

        website_url = params.get("website_url")
        element_selector = params.get("element_selector")

        if not website_url or not element_selector:
            return {"status": "error", "message": "Missing required parameters: 'website_url' and 'element_selector'."}

        response = composio_toolset.execute_action(
            action="WEBTOOL_SCRAPE_WEBSITE_ELEMENT",
            params={"website_url": website_url, "element_selector": element_selector},
            entity_id="default"
        )

        return {"status": "success", "data": response}

    except Exception as e:
        return {"status": "error", "message": str(e)}


# # Example Usage
# params = {
#     "website_url": "https://www.smartinfologiks.com/",
#     "element_selector": "p"
# }
# result = run_scraper(params)
# print(result)
