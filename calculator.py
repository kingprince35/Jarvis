import wolframalpha
import pyttsx3 as pt
import speech_recognition

engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("rate" , 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

apikey = ""