from modules.menus.menu import Menu
from algos_for_testing.car_play_music import PlayMusic
from algos_for_testing.car_play_music import PlayMusicNonStop
from algos_for_testing.car_measure_distance import MeasureDistance

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
        ]
    Menu(message, options)
