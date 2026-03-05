from picarx import Picarx
from robot_hat import TTS
from robot_hat import Music

bob = Picarx()
tts = TTS()
music = Music()

greeting = 'Hi, Diego!'

def sayHi():
    music.music_set_volume(25)
    music.sound_play('../../../sounds/car-start-engine.wav')
    tts.lang("en-US")
    tts.speak(greeting)
    music.sound_play('../../../sounds/car-double-horn.wav')


