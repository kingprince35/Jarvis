import requests
import json

from speech import speak
from config import NEWS_API_KEY

CATEGORIES = ["business", "entertainment", "health", "science", "sports", "technology"]


def latesnews():
    """Fetch and read latest news by category."""
    if not NEWS_API_KEY or NEWS_API_KEY == "your_news_api_key_here":
        speak("News API key is not configured. Please add it to your .env file.")
        return

    speak("Which category? Business, entertainment, health, science, sports, or technology?")
    field = input("Type news category: ").lower().strip()

    # Find matching category
    category = None
    for cat in CATEGORIES:
        if cat in field:
            category = cat
            break

    if not category:
        speak("I didn't understand that category. Please try again.")
        return

    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        news = response.json()

        if news.get("status") != "ok" or not news.get("articles"):
            speak("Sorry, I couldn't fetch any news right now.")
            return

        speak(f"Here are the top {category} headlines.")

        for article in news["articles"]:
            title = article.get("title", "No title")
            news_url = article.get("url", "")
            print(f"\n{title}")
            speak(title)
            if news_url:
                print(f"Read more: {news_url}")

            choice = input("[1 to continue] [2 to stop]: ").strip()
            if choice == "2":
                break

        speak("That's all the news for now.")

    except Exception as e:
        speak("Sorry, I couldn't fetch the news. Check your internet connection.")
        print(f"News Error: {e}")
