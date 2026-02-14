import pywhatkit
import wikipedia
import webbrowser

from speech import speak


def searchGoogle(query):
    """Search Google and read Wikipedia summary."""
    query = query.replace("jarvis", "").replace("google search", "").replace("google", "").strip()
    speak("This is what I found on Google")
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except Exception:
        speak("I found results in the browser but no speakable summary available.")


def searchYoutube(query):
    """Search and play a YouTube video."""
    query = query.replace("youtube search", "").replace("youtube", "").replace("jarvis", "").strip()
    speak("Playing from YouTube")
    try:
        pywhatkit.playonyt(query)
        speak("Done, playing now")
    except Exception:
        web = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
        webbrowser.open(web)
        speak("Opened YouTube search results")


def searchWikipedia(query):
    """Search Wikipedia and read summary."""
    query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("jarvis", "").strip()
    speak("Searching Wikipedia")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except Exception:
        speak("Sorry, I couldn't find that on Wikipedia.")
