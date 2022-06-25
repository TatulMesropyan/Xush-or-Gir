from random import randint

options = ["Xush", "Gir"]
randomizer = options[randint(0, 1)]

player = False

while player == False:
    player = input("Xush te Gir?")
    if player == "Xush":
        if randomizer == "Xush":
            print("You Win!")
        else:
            print("You Loose(")
    elif player == "Gir":
        if randomizer == "Gir":
            print("You Win")
        else:
            print("You Loose")
    else:
        print("You Loose(")
    player = False
    randomizer = options[randint(0, 1)]
