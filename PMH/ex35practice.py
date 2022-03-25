from sys import exit

current_cash = 0

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead("Man learn to type a number.")

    if how_much < 50:
        wallet(how_much, current_cash)
        current_cash = how_much + 0
        print("""
Nice, you're not greedy you win!, lets go spend our money in the town.
You close your eyes and mumble the magic words as reality begins to fade.\n\n""")

        town()

    else:
        dead("You greedy bastard!")


def town():
    print("You are in the town square, you see a bakery and a bank.\nWhere would you like to go? ")
    choice = input("> ")
    while True:
        if choice.lower() == "bakery":
            bakery()
        elif choice.lower() == "bank":
            bank()


def bakery():
    while True:
        print("It smells good ! What shall we do?")
        print("Menu\nBuy\nLeave")
        choice = input("> ")
        cake = 2
        bread = 1
        cake_stock = 5
        bread_stock = 5
        if choice.lower() == "menu":
            print("Bread = 1 Gold, Cake = 2 Gold")
            return
        elif choice.lower() == "buy":
            print("What would you like to buy?")
            order = input(">")
            if order.lower() == "cake":
                if cake_stock >= 1:
                    wallet(-cake, current_cash)
                    cake_stock -= 1
                if cake_stock == 0:
                    print("Cakes out of stock!")
        elif choice.lower() == "leave":
            return town()


def wallet(loot, current_cash):
    current_cash += loot
    print(f"You have {current_cash} gold in your wallet.")


def check_wallet():
    print(wallet())


def bear_room():
    print("""There is a bear here.
The bear has a bunch of honey.
The far bear is in front of another door.
How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:  # true and not false  (TRUE)
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't know what that means...")


def cthulhu_room():
    print("""Here you see the great evil Cthulhu. \nHe, it, whatever stares at you and you go insane. 
Do you flee for your life or eat your head?""")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    print("Would you like to play again?")
    play_again = input("> ")
    if play_again.lower() == "y":
        return start()

    else:
        exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice.lower() == "left":
        bear_room()
    elif choice.lower() == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")




start()
