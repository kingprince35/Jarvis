import os
import pyautogui
import webbrowser
import pyttsx3 as pt
import time

engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("rate" , 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"command prompt":"cmd" , "Paint" : "paint" , "excel":"excel" , "chrome" : "chrome" , "vscode" : "code" , "powerpoint" : "powerpnt"}

def openappweb(query):
    speak("Open the app")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"Start {dictapp[app]}")

def closeappweb(query):
    speak("Closingg")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "switch tab" in query:
        pyautogui.hotkey("ctrl","tab")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")