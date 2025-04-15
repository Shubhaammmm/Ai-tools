from langchain.tools import BaseTool
from langchain_community.tools import ElevenLabsText2SpeechTool as BaseElevenLabsText2SpeechTool
from playsound import playsound


class ElevenLabsText2SpeechTool(BaseTool):
    name: str = "text_to_speech"
    description: str = "Converts text to speech using Eleven Labs API."

    def _run(self, text: str):
        
        tts = BaseElevenLabsText2SpeechTool()
        speech_file = tts.run(text)

        # Play the generated speech file
        playsound(speech_file)

        return speech_file

    async def _arun(self, text: str):
        raise NotImplementedError("Async operation is not supported for this tool.")
