from langchain_core.tools import Tool
from langchain_experimental.utilities import PythonREPL

# Initialize the Python REPL
python_repl = PythonREPL()

def run(message: str, params: dict):
    """
    Executes the provided Python code in the REPL and returns the result.

    Args:
        message (str): The Python code to be executed.
        params (dict): Additional parameters (not used here but kept for standardization).

    Returns:
        dict: Status and the result of the Python code execution or an error message.
    """
    try:
        # Run the provided Python code in the REPL
        result = python_repl.run(message)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
