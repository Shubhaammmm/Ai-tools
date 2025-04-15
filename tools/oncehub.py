import typing as t
from composio_openai import ComposioToolSet, action, Action
from openai import OpenAI
import os
import requests

from dotenv import load_dotenv
load_dotenv()

# Load OnceHub credentials from environment variables
# 
os.environ["ONCEHUB_API_KEY"]="a539a03f1561e716f8205c19282dc0fb"
ONCEHUB_BASE_URL = "https://api.oncehub.com/v2"

os.environ["OPENAI_API_KEY"] = "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"


openai_client = OpenAI()
toolset = ComposioToolSet()

@action(toolname="oncehub")
def get_booking_details(
    booking_id: str,
    execute_request: t.Callable,
) -> dict:
    """
    Retrieve details of an existing OnceHub booking.

    :param booking_id: The ID of the booking to retrieve.
    :return booking_data: The details of the requested booking.
    """
    response = execute_request(
        f"{ONCEHUB_BASE_URL}/bookings/{booking_id}",
        "GET",
        None,
        None
    )
    return response

tools = toolset.get_tools(actions=[get_booking_details])

task = "Get details for booking ID 12345."

response = openai_client.chat.completions.create(
    model="gpt-4o",
    tools=tools,
    messages=[
        {"role": "system", "content": "You are a helpful agent."},
        {"role": "user", "content": task},
    ],
)

toolset.execute_action(
    action=get_booking_details,
    params={
        "booking_id": "12345",
    },
    entity_id="default",
)

result = toolset.handle_tool_calls(response)
print(result)
