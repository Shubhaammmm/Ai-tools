from langchain_core.tools import tool
import random

# Function to generate a random password
def generate_random_password(length: int = 12, include_special_chars: bool = True) -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    if include_special_chars:
        chars += special_chars
    return "".join(random.choices(chars, k=length))

# Initialize the tool and define the run function
def run(message: str, params: dict) -> dict:
    """
    Executes the random password generation and returns the result.

    Args:
        message (str): A description of the task (can be used for logging or debugging).
        params (dict): Parameters containing 'length' and 'include_special_chars'.

    Returns:
        dict: Status and the generated password or an error message.
    """
    try:
        # Extract parameters from the provided dictionary
        length = params.get('length', 12)
        include_special_chars = params.get('include_special_chars', True)

        # Generate the random password
        password = generate_random_password(length, include_special_chars)

        return {"status": "success", "generated_password": password}
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
