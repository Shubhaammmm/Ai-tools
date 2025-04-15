import os
from composio_langchain import ComposioToolSet

# Set API Key for Composio
# os.environ["NVIDIA_API_KEY"] = "your_nvidia_api_key"

# Initialize Composio ToolSet
composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")

def run(message: str, params: dict):
    """
    Fetches weather information based on the provided location.

    Args:
        message (str): A description of the request (not used but kept for consistency).
        params (dict): A dictionary containing "location".

    Returns:
        dict: Status and the weather data or an error message.
    """
    try:
        # Extract location from params
        location = params.get("location", "")

        if not location:
            return {"status": "error", "message": "Location parameter is missing"}

        # Execute the weather API action
        response = composio_toolset.execute_action(
            action="WEATHERMAP_WEATHER",
            params={"location": location},
            entity_id="default"
        )

        return {"status": "success", "data": response}

    except Exception as e:
        return {"status": "error", "message": str(e)}