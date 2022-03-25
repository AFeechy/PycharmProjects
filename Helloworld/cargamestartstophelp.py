command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car Already Started...")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
Start - To Start The Car
Stop - To Stop The Car
Quit - To Quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")