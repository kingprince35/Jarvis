import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (loaded from .env file)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# User settings
USER_NAME = "Prince"
ASSISTANT_NAME = "Jarvis"
CITY = "Ahmedabad"

# GROQ model settings
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_TEMPERATURE = 0.7
GROQ_MAX_TOKENS = 256

# Speech settings
SPEECH_RATE = 200
SPEECH_LANGUAGE = "en-in"
