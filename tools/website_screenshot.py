# website_screenshot.py
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from PIL import Image
from io import BytesIO
import os

def run(message: str, params: dict):
    """
    Takes a screenshot of a provided URL and saves it to the specified path.

    Args:
        message (str): Instruction or query (not used in this tool but included for standardization).
        params (dict): Parameters containing the 'url' and optional 'save_path'.

    Returns:
        dict: Status and the path of the saved screenshot or an error message.
    """
    url = params.get("url", "").strip()
    save_path = params.get("save_path", "screenshot.png")

    if not url:
        return {"status": "error", "message": "URL is required for taking a screenshot"}

    try:
        screenshot_path = take_screenshot(url, save_path)
        if screenshot_path:
            return {"status": "success", "message": f"Screenshot saved to: {screenshot_path}"}
        else:
            return {"status": "error", "message": "Failed to take screenshot"}
    except Exception as e:
        return {"status": "error", "message": f"Error while taking screenshot: {str(e)}"}

def take_screenshot(url, save_path="screenshot.png"):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        wd = webdriver.Chrome(options=options)
        wd.set_window_size(1080, 720)
        wd.get(url)
        wd.implicitly_wait(10)
        screenshot = wd.get_screenshot_as_png()
    except WebDriverException as e:
        return None
    finally:
        if wd:
            wd.quit()

    with open(save_path, "wb") as f:
        f.write(screenshot)

    return save_path  # Return the path where the screenshot is saved
