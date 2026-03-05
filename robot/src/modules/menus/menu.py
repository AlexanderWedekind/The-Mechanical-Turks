from modules.menus.get_num_input import GetNumInput

def Menu(message, options):
    print(message)
    for option in options:
        print(f"- [{options.index(option) +1}] {option['description']}")
    choice = GetNumInput(options, 'type number, press ENTER: ')
    for i in range(len(options)):
        if choice -1 == i:
            try:
                options[i]['function']()
            except Exception:
                print(f'{Exception}')
        
