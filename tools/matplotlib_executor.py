import matplotlib.pyplot as plt
import sys
import io
import numpy as np
from PIL import Image
import base64

def run_code(message: str):
    """
    Executes Python code that generates a Matplotlib plot.

    Args:
        message (str): The Python code to execute.

    Returns:
        dict: The result containing the plot as a base64-encoded string or an error message.
    """
    try:
        # Redirect stdout to capture print output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Execute the provided code in a sandboxed environment
        local_env = {'plt': plt, 'np': np}
        exec(message, {}, local_env)

        # Retrieve the captured output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check if Matplotlib plot was created
        if 'plt' in message:
            buf = io.BytesIO()
            plt.draw()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close()

            # Encode the image as a base64 string
            img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            return {
                "status": "success",
                "image": img_base64
            }
        else:
            return {
                "status": "error",
                "message": "No Matplotlib plot was generated."
            }

    except Exception as e:
        return {
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }

def run(message: str, params: dict):
    """
    Main handler function for the Matplotlib plot generator.

    Args:
        message (str): The Python code to execute.
        params (dict): Additional parameters (currently unused).

    Returns:
        dict: The result containing the plot or an error message.
    """
    return run_code(message)
