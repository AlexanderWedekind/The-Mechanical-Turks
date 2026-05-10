from modules.getPathToFile import getPathToFile
from modules.state.robot.robot_parts import robotParts
import readchar

def PlayMusic():
    robotParts.music.music_set_volume(50)
    robotParts.music.sound_play(getPathToFile(['..', 'sounds', 'car-start-engine.wav']))
    robotParts.music.music_play(getPathToFile(['..', 'music', '423321__dominictreis__the-doofus-sneaks-around.mp3']))
    robotParts.music.sound_play(getPathToFile(['..', 'sounds', 'car-double-horn.wav']))

def PlayMusicNonStop():
    robotParts.music.music_set_volume(25)
    robotParts.music.sound_play(getPathToFile(['..', 'sounds', 'car-start-engine.wav']))
    robotParts.music.sound_play(getPathToFile(['..', 'sounds', 'car-double-horn.wav']))
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
            robotParts.music.music_play(getPathToFile(['..', 'music', '423321__dominictreis__the-doofus-sneaks-around.mp3']))

