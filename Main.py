import os
import eel

from Engine.Feature import *
from Engine.command import *
eel.init("Frontend")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('Index.html', mode=None, host='localhost', block=True)