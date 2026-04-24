from modules.menus.menu import Menu
from algos_for_testing.car_play_music import PlayMusic
from algos_for_testing.car_play_music import PlayMusicNonStop
from algos_for_testing.car_measure_distance import MeasureDistance
from algos_for_testing.car_say_hi import sayHi
from algos_for_testing.car_turn_on_a_dime import turnOnADime
from algos_for_testing.line_follow import detectLine

def TestMenu():
    message = 'choose a function / algo you want to test: '
    options = [
            {
                'description': 'test playing music',
                'function': PlayMusic
                },
            {
                'description': 'non-stop music playing',
                'function': PlayMusicNonStop
                },
            {
                'description': 'measure distance',
                'function': MeasureDistance
                },
            {
                'description': "play 'starts engine', 'greeting', and 'horn-beep' sounds",
                'function': sayHi
                },
            {
                'description': 'tight turn circle',
                'function': turnOnADime
                },
            {
                'description': 'test detecting lines with greyscale sensor',
                'function': detectLine
                }
        ]
    Menu(message, options)
