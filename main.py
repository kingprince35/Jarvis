import pyttsx3 as pt
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import time
import pyautogui


engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("rate" , 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,5)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Please Say it again...??")
        return "None"
    return query

def unlock_laptop():
    pyautogui.FAILSAFE = False
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('0912', interval=0.25)  
    pyautogui.press('enter')
    pyautogui.FAILSAFE = True

if __name__ == "__main__":
    secret_code = "unlock"
    while True:
        query = take_command().lower()
        if "wake up" in query:
            from Greetme import greetme 
            greetme()

            while True:
                query = take_command().lower()
                if "unlock my laptop jarvis" in query:
                    speak("Please say the secret code")
                    code = take_command()
                    if code == secret_code:
                        speak("Unlocking laptop")
                        # import unlock_laptop
                        unlock_laptop()
                        break
                    else:
                        speak("Incorrect code. Try again.")
                time.sleep(5)
                if "bye-bye" in query:
                    speak("Ok Prince, You can call me Anytime. Call me jarvis wake up...")
                    break
                elif "hello" in query:
                    speak("Hello Prince, how are you?")
                elif "i am fine" in query:
                    speak("that's nice.")
                elif "how are you" in query:
                    speak("Perfect ")
                elif "What's about you" in query:
                    speak("also fine")
                elif "thank you" in query:
                    speak("Your Welcome , Prince")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video Muted")
                elif "up volume" in query:
                    from keyboardd import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "down volume" in query:
                    from keyboardd import volumedown
                    speak("Turning volume down")
                    volumedown()
                    

                elif "open" in query:
                    from app import openappweb
                    openappweb(query)
                
                elif "close" in query:
                    from app import closeappweb
                    closeappweb(query)
                
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from newsRead import latesnews
                    latesnews()
                
                elif "calculate" in query:
                    pass
                
                elif "temperature" in query:
                    search = "temperature in Ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                
                elif "weather" in query:
                    search = "weather in Ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Time is {strTime}")

                elif "go to sleep" in query:
                    speak("Going to sleep....")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that" , "")
                    rememberMessage = query.replace("jarvis" , "")
                    speak("You told me "+rememberMessage)
                    remember = open("remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("You told me to " + remember.read())
                
               
                    