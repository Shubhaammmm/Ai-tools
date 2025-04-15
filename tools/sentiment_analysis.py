from transformers import pipeline

# Load the model using the Hugging Face pipeline
classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def run(message: str, params: dict):
    """
    Analyzes sentiment of the provided query using a pre-trained sentiment analysis model.

    Args:
        message (str): The input text whose sentiment needs to be analyzed.
        params (dict): Additional parameters (not used here but kept for standardization).

    Returns:
        dict: Status and the sentiment analysis result or an error message.
    """
    try:
        # Run the sentiment analysis model
        result = classifier(message)
        return {"status": "success", "result": result}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
