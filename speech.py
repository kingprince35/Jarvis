import pyttsx3 as pt
import speech_recognition
from config import SPEECH_RATE, SPEECH_LANGUAGE, ASSISTANT_NAME

# Initialize TTS engine once (shared across all modules)
engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", SPEECH_RATE)


def speak(audio):
    """Convert text to speech and print to console."""
    print(f"{ASSISTANT_NAME}: {audio}")
    engine.say(audio)
    engine.runAndWait()


def listen(timeout=0, phrase_time_limit=8):
    """Listen to microphone and convert speech to text. Returns None if not understood."""
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except speech_recognition.WaitTimeoutError:
            return None

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language=SPEECH_LANGUAGE)
        print(f"You said: {query}")
        return query.lower()
    except speech_recognition.UnknownValueError:
        print("Could not understand audio.")
        return None
    except speech_recognition.RequestError:
        print("Speech recognition service unavailable.")
        return None
