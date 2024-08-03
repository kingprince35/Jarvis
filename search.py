import speech_recognition
import pyttsx3 as pt
import pywhatkit
import wikipedia
import webbrowser

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

query = take_command().lower()

engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("rate" , 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis" , "")
        query = query.replace("google search" , "")
        query = query.replace("google" , "")
        speak("This is what  I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No Speakable output available.")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found gor your search!")
        query = query.replace("youtube search" , "")
        query = query.replace("youtube" , "")
        query = query.replace("jarvis" , "")
        web = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Prince")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching ffrom wikipedia....")
        query = query.replace("wikipedia" , "")
        query = query.replace("search wikipedia" , "")
        query = query.replace("jarvis" , "")
        results = wikipedia.summary(query,sentences = 2)
        speak("Accroding to wikipedia..")
        print(results)
        speak(results)
    

