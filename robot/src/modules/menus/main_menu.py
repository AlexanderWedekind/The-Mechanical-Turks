from modules.menus.menu import Menu
from modules.menus.test_menu import TestMenu
from labyrinth_traversal.traverse_labyrinth import TraverseLabyrinth
from modules.menu_examples.example_menu import ExampleMenu

def MainMenu():
    message = "Welcome to The Mechanical Turks' labyrinth traversal robot\n-- Main menu --"
    options = [
            {
                'description': 'Run the Labyrinth traversal algorithm',
                'function': TraverseLabyrinth
                },
            {
                'description': 'See the example menu working',
                'function': ExampleMenu
                },
            {
                'description': 'Run tests',
                'function': TestMenu
                }
        ]
    Menu(message, options) 


