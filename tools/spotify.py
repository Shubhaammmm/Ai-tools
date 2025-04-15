from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
import os 
from composio_langchain import ComposioToolSet, Action, App
os.environ["NVIDIA_API_KEY"] = "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"

llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")

def run(message:str,params:dict):
    composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")
    tools = composio_toolset.get_tools(actions=['SPOTIFY_GET_USER_S_TOP_ARTISTS'])
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    # task = "get top artists of the week."
    result = agent_executor.invoke({"input": message})
    return result