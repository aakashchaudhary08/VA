import pygame
import eel

pygame.mixer.init()

@eel.expose

def playAssistantSound():
    pygame.mixer.music.load("Frontend/Assets/audio/start_sound.mp3")
    pygame.mixer.music.play()
