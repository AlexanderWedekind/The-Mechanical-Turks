from picarx import Picarx
from robot_hat.robot_hat.music import Music
import readchar

music = Music()

def playMusic():
    music.music_set_volume(25)
    music.sound_play('../../../sounds/car-engine-start.wav')
    music.music_play('../../../music/423321__dominictreis__the-doofus-sneaks-around.mp3')
    music.sound_play('../../../sounds/car-double-horn.wav')

def playMusicNonStop():
    music.music_set_volume(25)
    music.sound_play('../../../sounds/car-engine-start.wav')
    music.sound_play('../../../sounds/car-double-horn.wav')
    print('-- press [m] to start/stop music; press [q] to quit menu --')
    musicOn = False
    while True:
        keyStroke = readchar.readkey().lower()
        if keyStroke == 'm':
            if musicOn == False:
                musicOn = True
            else:
                musicOn = False
        elif keyStroke == 'q':
            break
        while musicOn == True:
            music.music_play('../../../music/423321__dominictreis__the-doofus-sneaks-around.mp3')

            

    

