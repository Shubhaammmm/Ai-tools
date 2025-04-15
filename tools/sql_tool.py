from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
import os 
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from composio_langchain import ComposioToolSet, Action, App
llm = ChatNVIDIA()
prompt = hub.pull("hwchase17/openai-functions-agent")


# os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["NVIDIA_API_KEY"] = "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"

composio_toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")
tools = composio_toolset.get_tools(actions=['SQLTOOL_SQL_QUERY'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

connection_string = "mysql://nodejs:nodejs%402024@192.168.0.22:3307/nodejs_cv_logs"

# Task to execute SQL query
task = {
    "query": "SELECT * FROM log_cv_attendance WHERE username = 'pranit'",
    "connection_string": connection_string
}
result = agent_executor.invoke({"input": task})
print(result)



