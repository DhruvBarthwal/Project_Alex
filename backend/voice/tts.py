from deepgram import Deepgram
import os 

dg = Deepgram(os.getenv("DEPPGRAM_API_KEY"))

def text_to_speech(text):
    response = dg.speak.v("1").save("output.wav",{
        "text" : text
    })
    return "output.wav"