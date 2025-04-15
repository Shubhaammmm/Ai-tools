import requests
from bs4 import BeautifulSoup

def run(message: str, params: dict):
    """
    Extracts all content from the provided URL.

    Args:
        message (str): Instruction or query (not used in this tool but included for standardization).
        params (dict): Parameters containing the 'url' to scrape.

    Returns:
        dict: Status and either the extracted content or an error message.
    """
    url = params.get("url", "").strip()
    if not url:
        return {"status": "error", "message": "URL is required for scraping"}

    try:
        # Extract content from the URL
        content = scrape_all_content(url)
        return {"status": "success", "results": content}
    except Exception as e:
        return {"status": "error", "message": f"Failed to scrape content: {str(e)}"}

def scrape_all_content(url: str) -> str:
    """
    Fetch and extract all content from the provided URL.

    Args:
        url (str): The target webpage URL.

    Returns:
        str: Extracted text content from the webpage (limited to 2000 characters).
    """
    headers = {"User-Agent": "Mozilla/5.0 (compatible; WebScraperTool/1.0)"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        # Extract text content with a line separator for readability
        extracted_data = soup.get_text(separator="\n", strip=True)
        return extracted_data[:2000]  # Limit the content to 2000 characters
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch URL: {str(e)}")
