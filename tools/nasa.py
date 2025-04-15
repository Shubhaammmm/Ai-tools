import os
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.nasa.toolkit import NasaToolkit
from langchain_community.utilities.nasa import NasaAPIWrapper
from langchain_groq import ChatGroq

# Set the environment variable for GROQ API key
os.environ["GROQ_API_KEY"] = "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"
groq_api = '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'

# Initialize the language model (LLM) and the NASA API wrapper
llm = ChatGroq(temperature=0)
nasa = NasaAPIWrapper()

# Set up the NASA toolkit and initialize the agent
toolkit = NasaToolkit.from_nasa_api_wrapper(nasa)
agent = initialize_agent(
    toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

def run(query: str, params: dict = None) -> dict:
    """
    Search NASA's database for information based on a provided query.

    Args:
        query (str): The search query string.
        params (dict): Additional parameters (optional).

    Returns:
        dict: A dictionary with status and the results from NASA API.
    """
    try:
        if not query.strip():
            return {"status": "error", "message": "Query is required for NASA search"}

        # Run the query through the NASA agent
        response = agent.run(query)
        return {"status": "success", "results": response}
    except Exception as e:
        return {"status": "error", "message": f"Error performing NASA search: {str(e)}"}
