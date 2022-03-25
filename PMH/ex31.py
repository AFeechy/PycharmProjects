print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("""
    You stare into the endless abyss at Cthulhu's retina.
    1. Blueberries.
    2. Yellow Jacket Clothespins.
    3. Understanding revolvers yelling melodies.""")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives, powered by a mind of jello.")
        print("Good Job!")
    else:
        print("The insanity rots your eyes into a pool of much")
        print("Good Job!")


else:
    print("You stumble around and fall on a knife and die. Good Job!")

while True:
    print("""You have a choice of reincarnation:
    
    1 - Michael the Accountant
    2 - Jonathan the Spice Merchant
    3 - Mabel the Financial Advisor
    """)

    choice = input("Who will it be ?\n")

    if choice == "1":
        print("Congratulations, you die from an intestinal blockage, age 62.")
        break

    elif choice == "2":
        print("Your life is bland and your work does nothing to rectify that. You die alone age 89.")
        break

    elif choice == "3":
        print("""Life is void of meaning and pleasure in a world when the computer says 'No'. 
        You take your own life, age 35""")
        break

    else:
        # choice != 1, 2, 3     REDUNDANT
        print("You cannot run from your destiny... ")

print("Would you like another chance (Y)?")
ans2 = input('> ')
if ans2.lower() == "y":
    while True:
        lifespan = (input("How long would you like to live? >"))
        if lifespan.isnumeric():

            lifespan = int(lifespan)

            if lifespan <= 20:
                print("That's not long enough...")

            elif lifespan in range(20, 40):
                print("Live fast, die young...")
                break

            elif lifespan > 40:
                print("It's not the old testament, we can make that happen.")
                break

        else:
            print(f"I'm sorry... \"{lifespan}\", is not an option in this religion.")

else:
    print("Thanks for playing Alex's game of life.")