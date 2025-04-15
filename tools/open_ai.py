import os
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, App

# Set OpenAI API key in environment variables
os.environ["OPENAI_API_KEY"] = "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"

# Initialize OpenAI LLM correctly
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Composio toolset
toolset = ComposioToolSet(api_key="jzjstcadadwfz5arkpfse")
tools = toolset.get_tools(actions=['ASANA_ADD_A_USER_TO_A_WORKSPACE_OR_ORGANIZATION'])

# Pull prompt template
prompt = hub.pull("hwchase17/openai-functions-agent")

# Create agent
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute task
task = "add user to a workspace with name 'my workspace' with email id oundhakarshubham@gmail.com"
result = agent_executor.invoke({"input": task})

print(result)
