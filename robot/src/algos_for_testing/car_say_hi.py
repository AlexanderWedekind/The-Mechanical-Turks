from modules.getPathToFile import getPathToFile
from modules.state.robot.robot_parts import robotParts


def sayHi():
    greeting = 'Hi, Ryan!'

    robotParts.music.music_set_volume(50)
    robotParts.music.sound_play(getPathToFile(['..', 'sounds', 'car-start-engine.wav']))
    robotParts.music.music_set_volume(90)
    robotParts.tts.lang('en-US')
    robotParts.tts.say(greeting)
    robotParts.music.music_set_volume(50)
    robotParts.music.sound_play(getPathToFile(['..', 'sounds', 'car-double-horn.wav']))


