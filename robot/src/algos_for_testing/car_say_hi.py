from picarx import Picarx
from robot_hat import TTS
from robot_hat import Music
from modules.getPathToFile import getPathToFile


def sayHi():
    greeting = 'Hi, Diego!'

    bob = Picarx()
    tts = TTS()
    music = Music()

    music.music_set_volume(25)
    music.sound_play(getPathToFile(['sounds', 'car-start-engine.wav']))
    tts.lang("en-US")
    tts.speak(greeting)
    music.sound_play(getPathToFile(['sounds', 'car-double-horn.wav']))
    bob.stop()


