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

    try:
        eel.DisplayMessage(text)()
    except:
        pass

    engine.say(text)
    engine.runAndWait()


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

        speak(query)   # 👈 THIS LINE MAKES IT SPEAK

        time.sleep(1)

        return query.lower()

    except Exception:
        print("Sorry, I didn't understand")
        eel.DisplayMessage("Sorry, I didn't understand")()
        time.sleep(2)
        eel.ShowHood()()
        speak("Sorry, I didn't understand")
        return ""


@eel.expose
def allCommands():
    query = takeCommand()
    print(query)

    if "open" in query:
        from engine.feature import openCommand
        openCommand(query)

    elif "youtube" in query:
        from engine.feature import PlayYoutube
        PlayYoutube(query)

    else:
        print("not run")

    eel.ShowHood()()  