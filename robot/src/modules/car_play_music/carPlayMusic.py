from picarx import Picarx
from robot_hat import Music

music = Music()

def playMusic():
    music.music_set_volume(25)
    music.sound_play('../../../sounds/car-engine-start.wav')
    music.music_play('../../../music/423321__dominictreis__the-doofus-sneaks-around.mp3')
    music.sound_play('../../../sounds/car-double-horn.wav')




