import os
import webbrowser
import pyautogui

from speech import speak

dictapp = {
    "command prompt": "cmd",
    "paint": "paint",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc",
    "file explorer": "explorer",
}


def openappweb(query):
    """Open an application or website based on voice command."""
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "").replace("jarvis", "").replace("launch", "").strip()
        query = query.replace(" ", "")
        speak(f"Opening {query}")
        webbrowser.open(f"https://www.{query}")
    else:
        for app_name, exe_name in dictapp.items():
            if app_name in query:
                speak(f"Opening {app_name}")
                os.system(f"start {exe_name}")
                return
        speak("Sorry, I don't know that application.")


def closeappweb(query):
    """Close an application or browser tab."""
    if "one tab" in query or "1 tab" in query:
        speak("Closing tab")
        pyautogui.hotkey("ctrl", "w")
    elif "switch tab" in query:
        speak("Switching tab")
        pyautogui.hotkey("ctrl", "tab")
    elif "window" in query:
        speak("Closing window")
        pyautogui.hotkey("alt", "F4")
    else:
        for app_name, exe_name in dictapp.items():
            if app_name in query:
                speak(f"Closing {app_name}")
                os.system(f"taskkill /f /im {exe_name}.exe")
                return
        speak("Sorry, I don't know which app to close.")
