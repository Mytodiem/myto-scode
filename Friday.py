import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)

def speak(audio):
    print('F.R.I.D.A.Y. :  '+audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >=5 and hour<12:
            speak("Good Morning Boss")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Boss")
    elif hour >= 18 and hour <24:
        speak("Good night Boss")
    speak("how can i help you")
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Myto :"+query)
    except sr.UnknownValueError:
        print("Please repeat or typing the order")
        query=str(input("your order is :"))
    return query


if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("what should i search, Boss ?")
            search=command().lower()
            url=f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'here is your {search} on google')
        elif "youtube" in query:
            speak("what should i search, Boss ?")
            search=command().lower()
            url=f"https://www.youtube.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'here is your {search} on youtube')
        elif "open video"in query:
            video=r"C:\Users\my.todiem\Documents\code\video.mp4"
            os.startfile(video)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Friday is quitting. Goodbye Boss!")
            quit()
        