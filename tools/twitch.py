import typing as t
from composio_openai import ComposioToolSet, action, Action
from openai import OpenAI
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = "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"

openai_client = OpenAI()
toolset = ComposioToolSet()


@action(toolname="twitch")
def get_stream_info(
    channel_name: str,
    execute_request: t.Callable,
) -> dict:
    """
    Fetch live stream details for a given Twitch channel.

    :param channel_name: The name of the Twitch channel.
    :return stream_info: The details of the live stream (if active).
    """
    response = execute_request(f"https://api.twitch.tv/helix/streams?user_login={channel_name}", "GET", None, None)
    return response.get("data", {})


tools = toolset.get_tools(actions=[get_stream_info])

task = "Get live stream details for the Twitch channel 'tarik'."

response = openai_client.chat.completions.create(
    model="gpt-4o",
    tools=tools,
    messages=[
        {"role": "system", "content": "You are a helpful agent."},
        {"role": "user", "content": task},
    ],
)

toolset.execute_action(
    action=get_stream_info,
    params={
        "channel_name": "tarik",
    },
    entity_id="default",
)

result = toolset.handle_tool_calls(response)
print(result)
