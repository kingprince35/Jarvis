import pyttsx3 as pt
import datetime
engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("rate" , 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 11:
        speak("Good Morning, Prince")
    elif hour >= 12 and hour <= 18:
        speak("Good AfterNoon, Prince")
    else:
        speak("Good Evening, Prince")
    speak("Please, tell me How can i Help you??")
