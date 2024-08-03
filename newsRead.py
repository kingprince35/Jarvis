import requests
import json
import pyttsx3 as pt


engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
engine.setProperty("rate" , 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latesnews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4e465f3d997f4b83be98eb1bcf71d877" ,
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4e465f3d997f4b83be98eb1bcf71d877",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4e465f3d997f4b83be98eb1bcf71d877",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4e465f3d997f4b83be98eb1bcf71d877",
               "sport":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4e465f3d997f4b83be98eb1bcf71d877",
               "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4e465f3d997f4b83be98eb1bcf71d877"}
    
    content = None
    url = None
    speak("which field news do you want,[business] , [health] , [technology] , [sports] , [entertainment] , [science] ")
    field = input("Type field news that you want : ")
    for key , value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is hte first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2": 
            break
    speak("thats all")

    