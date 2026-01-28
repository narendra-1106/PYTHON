# Install required libraries first:
# pip install pyttsx3 SpeechRecognition wikipedia pyaudio

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Narendra How are you!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()

    except Exception:
        print("Say that again please...")
        return "none"

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-app-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()

# Main program
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\Songs"   # change path
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open code' in query:
            codePath = r"C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye")
            break

        else:
            speak("I did not understand that")
