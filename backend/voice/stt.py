from deepgram import Deepgram
import os , asyncio

dg = Deepgram(os.getenv("DEEPGRAM_API_KEY"))

async def speech_to_text(audio_bytes):
    source = {"buffer" : audio_bytes, "mimetype" : "audio/wav"}
    response = await dg.transcription.prerecorded(
        source,
        {"punctuate" : True}
    )
    return response["result"]["channels"][0]["alternatves"][0]["transcript"]