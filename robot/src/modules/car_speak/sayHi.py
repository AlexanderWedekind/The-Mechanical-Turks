from picarx import Picarx
from robot_hat import TTS

bob = Picarx()
tts = TTS()

greeting = 'Hi, Diedo!'

def sayHi():
    tts.speak(greeting)


