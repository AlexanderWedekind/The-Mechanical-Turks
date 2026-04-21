from modules.getPathToFile import getPathToFile
from modules.hardware_startup import robotParts


def sayHi():
    greeting = 'Hi, Ryan!'

    robotParts['music'].music_set_volume(25)
    robotParts['music'].sound_play(getPathToFile(['..', 'sounds', 'car-start-engine.wav']))
    robotParts['tts'].lang("en-US")
    robotParts['tts'].espeak('espeak', greeting)
    robotParts['music'].sound_play(getPathToFile(['..', 'sounds', 'car-double-horn.wav']))


