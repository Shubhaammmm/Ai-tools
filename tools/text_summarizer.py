from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

def summarize_text(message: str, params: dict):
    """
    Summarizes the input text using the Falconsai/text_summarization model.

    Args:
        message (str): The input text to summarize.
        params (dict): Additional parameters for summarization like max_length and min_length.

    Returns:
        dict: The result containing the summarized text.
    """
    try:
        # Extract parameters with default values
        max_length = params.get("max_length", 1000)
        min_length = params.get("min_length", 30)
        do_sample = params.get("do_sample", False)

        # Perform summarization
        summary = summarizer(message, max_length=max_length, min_length=min_length, do_sample=do_sample)

        return {
            "status": "success",
            "result": summary[0]["summary_text"]
        }
    except Exception as e:
        # Handle errors gracefully
        return {
            "status": "error",
            "message": f"An error occurred during summarization: {str(e)}"
        }

def run(message: str, params: dict):
    """
    Main handler function for the summarization tool.

    Args:
        message (str): The input text to summarize.
        params (dict): Additional parameters for summarization.

    Returns:
        dict: The summarization result or error message.
    """
    return summarize_text(message, params)
