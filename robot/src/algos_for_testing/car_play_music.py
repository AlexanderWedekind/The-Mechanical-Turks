from picarx import Picarx
from robot_hat import Music
from modules.getPathToFile import getPathToFile
import readchar
from pathlib import Path

currentDir = Path(__file__).parent
print(f"-- Current Dir: '{currentDir}'")

pathToMain = Path('home/The-Mechanical-Turks/robot/src/')
filePath = pathToMain / '..' / 'sounds' / 'car-start-engine.py'

def PlayMusic():
    music = Music()
    music.music_set_volume(25)
    music.sound_play(getPathToFile(['sounds', 'car-start-engine.wav']))
    music.music_play(getPathToFile(['music', '423321__dominictreis__the-doofus-sneaks-around.mp3']))
    music.sound_play(getPathToFile(['sounds', 'car-double-horn.wav']))
    music.stop()

def PlayMusicNonStop():
    music = Music()
    music.music_set_volume(25)
    music.sound_play(getPathToFile(['sounds', 'car-start-engine.wav']))
    music.sound_play(getPathToFile(['sounds', 'car-double-horn.wav']))
    print('-- press [m] to start/stop music; press [q] to quit menu --')
    musicOn = False
    keyStroke = ' '
    while keyStroke != 'q':
        keyStroke = readchar.readkey().lower()
        if keyStroke == 'm':
            if musicOn == False:
                musicOn = True
            else:
                musicOn = False
        elif keyStroke == 'q':
            break
        while musicOn == True:
            music.music_play('~/repos/The-Mechanical-Turks/music/423321__dominictreis__the-doofus-sneaks-around.mp3')
    music.stop()

            

    

