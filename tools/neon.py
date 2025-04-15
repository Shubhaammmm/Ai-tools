from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from composio_langchain import ComposioToolSet, Action, App
os.environ["NVIDIA_API_KEY"] = "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"

llm = ChatNVIDIA()
prompt = hub.pull("hwchase17/openai-functions-agent")

composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")
tools = composio_toolset.get_tools(apps=[App.NEON])


def run(message:str,params:dict):
    tools = composio_toolset.get_tools(apps=[App.NEON])
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    result = agent_executor.invoke({"input": message})
    return result