from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_openai import ChatOpenAI
import os
from composio_langchain import ComposioToolSet, Action, App

composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")

def run(message:dict,params:dict):
    query={
        "query":message
    }
    response=composio_toolset.execute_action(
        action="SERPAPI_SHOPPING_SEARCH",
        params=query,
        entity_id="default"
)
    return response