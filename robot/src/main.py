from picarx import Picarx
import time

from modules.car_speak.sayHi import sayHi
from modules.car_play_music.carPlayMusic import playMusic

px = Picarx()
speed = 30
stop = 0
backUp = 15
turnNow = 30



def main():
    sayHi()   
    playMusic()

main()

