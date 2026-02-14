import datetime
import requests
from bs4 import BeautifulSoup
import pyautogui
import time

from speech import speak, listen
from brain import ask, clear_history
from memory import save_memory, get_last_memory, get_all_memories_text
from config import USER_NAME, CITY, GROQ_API_KEY


def greet():
    """Greet the user based on time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak(f"Good Morning, {USER_NAME}")
    elif hour < 18:
        speak(f"Good Afternoon, {USER_NAME}")
    else:
        speak(f"Good Evening, {USER_NAME}")
    speak("Jarvis online. How can I help you?")


def get_temperature():
    """Get current temperature for the configured city."""
    try:
        url = f"https://www.google.com/search?q=temperature+in+{CITY}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"Current temperature in {CITY} is {temp}")
    except Exception:
        # If scraping fails, ask AI instead
        response = ask(f"What is the typical weather in {CITY} right now?")
        speak(response)


def get_weather():
    """Get current weather for the configured city."""
    try:
        url = f"https://www.google.com/search?q=weather+in+{CITY}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"Current weather in {CITY} is {temp}")
    except Exception:
        response = ask(f"What is the typical weather in {CITY} right now?")
        speak(response)


def handle_command(query):
    """Route voice commands to the appropriate handler."""

    # --- Exit commands ---
    if "go to sleep" in query or "bye-bye" in query or "shutdown" in query:
        speak(f"Going to sleep. Call me anytime, {USER_NAME}. Just say wake up.")
        return False

    # --- App control (needs exact system actions) ---
    elif "open" in query:
        from app import openappweb
        openappweb(query)

    elif "close" in query:
        from app import closeappweb
        closeappweb(query)

    # --- Media controls ---
    elif "pause" in query or "play" in query:
        pyautogui.press("k")
        speak("Done")

    elif "mute" in query:
        pyautogui.press("m")
        speak("Video muted")

    elif "volume up" in query or "up volume" in query:
        from keyboardd import volumeup
        speak("Turning volume up")
        volumeup()

    elif "volume down" in query or "down volume" in query:
        from keyboardd import volumedown
        speak("Turning volume down")
        volumedown()

    # --- Web search ---
    elif "google" in query:
        from search import searchGoogle
        searchGoogle(query)

    elif "youtube" in query:
        from search import searchYoutube
        searchYoutube(query)

    elif "wikipedia" in query:
        from search import searchWikipedia
        searchWikipedia(query)

    # --- News ---
    elif "news" in query:
        from newsRead import latesnews
        latesnews()

    # --- Weather/Temperature ---
    elif "temperature" in query:
        get_temperature()

    elif "weather" in query:
        get_weather()

    # --- Time ---
    elif "time" in query and ("what" in query or "tell" in query):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # --- Memory ---
    elif "remember that" in query or "remember this" in query:
        message = query.replace("remember that", "").replace("remember this", "")
        message = message.replace("jarvis", "").strip()
        if message:
            save_memory(message)
            speak(f"I'll remember that: {message}")
        else:
            speak("What should I remember?")

    elif "what do you remember" in query or "what did i say" in query:
        last = get_last_memory()
        if last:
            speak(f"You told me: {last}")
        else:
            speak("I don't have any saved memories yet.")

    elif "all memories" in query or "show memories" in query:
        memories = get_all_memories_text()
        speak(memories)

    # --- Clear AI conversation ---
    elif "clear history" in query or "forget conversation" in query:
        clear_history()
        speak("Conversation history cleared. Starting fresh.")

    # --- EVERYTHING ELSE goes to GROQ AI ---
    else:
        response = ask(query)
        speak(response)

    return True


def main():
    """Main entry point for Advanced Jarvis."""
    # Check if GROQ API key is configured
    if not GROQ_API_KEY or GROQ_API_KEY == "your_groq_api_key_here":
        print("=" * 50)
        print("WARNING: GROQ API key not configured!")
        print("Add your key to .env file:")
        print('  GROQ_API_KEY=your_actual_key_here')
        print("Get your key at: https://console.groq.com")
        print("=" * 50)
        print("Starting without AI features...\n")

    print(f"{'=' * 50}")
    print(f"  JARVIS - Advanced AI Assistant for {USER_NAME}")
    print(f"  Say 'wake up' to activate")
    print(f"{'=' * 50}\n")

    while True:
        query = listen()
        if query is None:
            continue

        if "wake up" in query:
            greet()

            # Main command loop
            while True:
                query = listen()
                if query is None:
                    continue

                keep_running = handle_command(query)
                if not keep_running:
                    break


if __name__ == "__main__":
    main()
