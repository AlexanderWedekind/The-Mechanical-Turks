def GetNumInput(options, message):
    valid = False
    userInput = -1
    while valid == False:
        try:
            userInput = int(input(message))
            if userInput > 0 and userInput < len(options) + 1:
                valid = True
            else:
                valid = False
                print("that wasn't within the range of choices, try again")
        except:
            print("that wasn't a valid choice, try again")
            valid = False
    return userInput


