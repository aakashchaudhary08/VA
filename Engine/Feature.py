import pygame
import eel
import os
import re
import pywhatkit as kit
from engine.config import ASSISTANT_NAME
from engine.command import speak

pygame.mixer.init()


@eel.expose
def playAssistantSound():
    pygame.mixer.music.load("frontend/assets/audio/start_sound.mp3")
    pygame.mixer.music.play()


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("Application not found")


def extract_yt_term(command):
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else command.replace("play", "").replace("youtube", "").strip()


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)