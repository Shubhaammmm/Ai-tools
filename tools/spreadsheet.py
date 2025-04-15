# NOT Deployed

from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os 
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App
os.environ["NVIDIA_API_KEY"] = "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"

# os.environ["OPENAI_API_KEY"] = "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"

llm = ChatNVIDIA()
os.environ["LANGCHAIN_API_KEY"] = "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"

# llm = ChatNVIDIA()
prompt = hub.pull("hwchase17/openai-functions-agent")

def run(message:str,params:dict):
    composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")
    tools = composio_toolset.get_tools(apps=[App.GOOGLESHEETS])

    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    # task = "get information about spreadsheet of id = 1d-BeRkQT77Cnf2I2byhalZpBCoS1M5q62YoYt_GDuNA"
    result = agent_executor.invoke({"input": message})
    return result
