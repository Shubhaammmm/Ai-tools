from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits import NLAToolkit
from langchain_community.utilities import Requests
from langchain_groq import ChatGroq
groq_api = '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'


chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768",api_key=groq_api)

speak_toolkit = NLAToolkit.from_llm_and_url(chat, "https://api.speak.com/openapi.yaml")