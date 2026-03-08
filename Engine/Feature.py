from playsound import playsound
import eel

# Playing assistant sound function

@eel.expose

def playAssistantSound():
    music_dir = "Frontend\\Assets\\audio\\start_sound.mp3"
    playsound(music_dir)
