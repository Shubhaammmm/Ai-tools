import requests
from bs4 import BeautifulSoup
import validators
import tldextract
from urllib.parse import urlparse

def validate_url(url):
    """Validate the URL."""
    if not validators.url(url):
        raise ValueError("Invalid URL provided.")
    return url

def fetch_webpage(url):
    """Fetch the HTML content of the webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching webpage: {e}")

def extract_metadata(soup):
    """Extract metadata like title, description, and keywords."""
    return {
        "title": soup.title.string if soup.title else "No title found",
        "description": soup.find("meta", {"name": "description"})["content"] if soup.find("meta", {"name": "description"}) else "No description found",
        "keywords": soup.find("meta", {"name": "keywords"})["content"] if soup.find("meta", {"name": "keywords"}) else "No keywords found",
    }

def extract_backlinks(soup, base_url):
    """Identify external backlinks."""
    backlinks = []
    for link in soup.find_all("a", href=True):
        parsed_url = urlparse(link["href"])
        domain_info = tldextract.extract(parsed_url.netloc)
        if domain_info.domain and domain_info.domain not in base_url:
            backlinks.append(link["href"])
    return list(set(backlinks))

def analyze_webpage(url):
    """Fetch and analyze the webpage for SEO metrics."""
    validate_url(url)
    soup = fetch_webpage(url)
    metadata = extract_metadata(soup)
    backlinks = extract_backlinks(soup, url)
    return {
        "metadata": metadata,
        "backlinks": backlinks,
    }

def run(message, params):
    """
    Executes the Webpage SEO Analyzer tool.

    Args:
        message (str): Optional additional input (unused in this tool).
        params (dict): Contains the URL to analyze.

    Returns:
        dict: The SEO analysis results or error messages.
    """
    url = params.get("url")
    if not url:
        return {
            "status": "error",
            "message": "URL not provided."
        }
    try:
        seo_report = analyze_webpage(url)
        return {
            "status": "success",
            "result": seo_report
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error during analysis: {str(e)}"
        }