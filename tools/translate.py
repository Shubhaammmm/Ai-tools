from transformers import pipeline

# Initialize the translation pipeline
translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

def translate_english_to_french(text: str) -> str:
    """
    Translates English text to French using a pre-trained transformer model.

    Args:
        text (str): The English text to translate.

    Returns:
        str: Translated French text.
    """
    try:
        # Perform the translation
        translation = translation_pipeline(text)[0]["translation_text"]
        return translation
    except Exception as e:
        return f"Error: {str(e)}"

def run(message: str, params: dict):
    """
    Dynamic run function to execute the translation tool.

    Args:
        message (str): The English text to translate.
        params (dict): Additional parameters (not used in this tool).

    Returns:
        dict: The result of the translation or an error message.
    """
    try:
        # Perform the translation
        translated_text = translate_english_to_french(message)

        # Return the response
        return {"status": "success", "result": translated_text}
    except Exception as e:
        # Handle unexpected errors
        return {"status": "error", "message": str(e)}
