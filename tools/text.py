import os
import edge_tts
import tempfile

# Function to convert text to speech
def text_to_speech(message, voice, rate, pitch, save_dir):
    """
    Convert the given message to speech using the specified voice, rate, and pitch.
    
    :param message: The text to convert to speech.
    :param voice: The voice to use for speech.
    :param rate: The speech rate.
    :param pitch: The pitch adjustment.
    :param save_dir: Directory where the audio file should be saved.
    
    :return: Path to the generated audio file or error message.
    """
    if not message.strip():
        return None, "Please enter text to convert."
    if not voice:
        return None, "Please select a voice."
    
    # Set voice and rate
    voice_short_name = voice.split(" - ")[0]
    rate_str = f"{rate:+d}%"
    pitch_str = f"{pitch:+d}Hz"
    
    # Initialize the speech communication
    communicate = edge_tts.Communicate(message, voice_short_name, rate=rate_str, pitch=pitch_str)
    
    # Ensure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Define the file path
    audio_file_path = os.path.join(save_dir, "output_audio.mp3")
    
    # Save the audio file
    communicate.save(audio_file_path)
    
    return audio_file_path, None

# Function to handle the JSON input and execute the text-to-speech conversion
def run(message, params):
    """
    Function to execute the speech conversion based on the provided message and parameters.
    
    :param message: The text message to convert to speech.
    :param params: Dictionary containing voice, rate, and pitch for conversion.
    
    :return: JSON response with the audio file path or error message.
    """
    try:
        # Extract parameters from the input JSON
        voice = params.get("voice")
        rate = params.get("rate", 0)
        pitch = params.get("pitch", 0)
        save_dir = params.get("save_dir", "./audio_files")  # Default directory if not provided

        # Validate the inputs
        if not message:
            return {"status": "error", "message": "Message cannot be empty."}
        if not voice:
            return {"status": "error", "message": "Voice must be specified."}

        # Call the text-to-speech conversion function
        audio_file_path, error = text_to_speech(message, voice, rate, pitch, save_dir)

        if error:
            return {"status": "error", "message": error}

        # Return the audio file path as part of the success response
        return {
            "status": "success",
            "data": {"audio_file": audio_file_path}
        }

    except Exception as e:
        # Handle unexpected errors
        return {"status": "error", "message": f"An error occurred: {str(e)}"}