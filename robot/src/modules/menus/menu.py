from modules.menus.get_num_input import GetNumInput

def Menu(message, options, exitMessage = 'return to previous menu'):
    userChoice = 1
    def actionUserChoice():
        print(message)
        for option in options:
            print(f"- [{options.index(option) +1}] {option['description']}")
        print(f"- [{len(options) +1}] {exitMessage}")
        choice = GetNumInput(options, 'type number, press ENTER: ')
        for i in range(len(options)):
            if choice -1 == i:
                try:
                    options[i]['function']()
                except Exception:
                    print(f'{Exception}')
        return choice
    while userChoice > 0 and userChoice < len(options) +1:
        userChoice = actionUserChoice()
 
       
