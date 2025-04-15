from langchain_community.tools import ShellTool

def run(message: str, params: dict):
    """
    Executes shell commands and returns the output.

    Args:
        message (str): A string containing shell commands separated by commas.
        params (dict): Additional parameters (not used here but kept for standardization).

    Returns:
        dict: Status and the result of the execution or an error message.
    """
    shell_tool = ShellTool()

    try:
        # Split the message by commas to get individual commands
        commands = [command.strip() for command in message.split(',') if command.strip()]

        # Validate that commands is a non-empty list
        if not commands:
            return {"status": "error", "message": "Invalid input. 'message' must contain non-empty commands."}

        # Run the shell commands using the ShellTool
        result = shell_tool.run({"commands": commands})
        return {"status": "success", "output": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}
