import pyttsx3
import speech_recognition as sr
import eel
import time

print("Program started")

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)

    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()


@eel.expose
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")()
        audio = r.listen(source)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")()

        query = r.recognize_google(audio, language="en-in")

        print("User said:", query)

        eel.DisplayMessage(query)()

        speak(query)

        time.sleep(1)

        eel.ShowHood()()

        return query.lower()

    except:
        print("Sorry, I didn't understand")
        eel.DisplayMessage("Sorry, I didn't understand")()
        eel.ShowHood()()
        return ""