from modules.menus.menu import Menu
from modules.menu_examples.function_one import FunctionOne
from modules.menu_examples.function_two import FunctionTwo
from modules.menu_examples.function_three import FunctionThree

def ExampleMenu():
    message = 'choose an option'
    options = [
        {
            'description': 'option ONE',
            'function': FunctionOne
        },
        {
            'description': 'option TWO',
            'function': FunctionTwo,
        },
        {
            'description': 'option THREE',
            'function': FunctionThree
        }
    ]
    Menu(message, options)
    


