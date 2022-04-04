import time
import sys
import os

check_file = "bank.txt"
if os.path.isfile(check_file):
    print(f""""Existing Save File Detected '{check_file}'... 

Would you like to OPEN or create NEW save file?""")
    choice = input('>')

    if choice.lower() == "open":
        print("Saved Bank Opened")
        input_file_1 = open(check_file, 'r+')
        print(input_file_1.read())
        input_file_1.seek(0)


    elif choice.lower() == "new":
        print("This will delete your old save, are you sure ? Y/N")
        choice_2 = input('>')

        if choice_2.lower() == 'y':
            input_file_1 = open(check_file, 'w+')
            input_file_1.write('0')

        elif choice_2.lower() == 'n':
            sys.exit('We must say goodbye to the past before we can look to the future...')

        else:
            sys.exit('Input Not Accepted')


else:
    input_file_1 = open(check_file, 'w+')
    print(input_file_1.read())
    input_file_1.write('0')
    print(input_file_1.read())

    print("New Bank Save Created")

inventory = []

global wallet

global beach_red_rock
global beach_grey_rock
global beach_white_rock
global mountain_black_rock

wallet = 0

beach_red_rock = 5
beach_grey_rock = 5
beach_white_rock = 1
mountain_black_rock = 8

def city_centre():
    time.sleep(0.5)
    print("The hustle and bustle of the city continues around you... You see a BAKERY, PAWN SHOP and a BANK.")
    choice = input("> ")

    if choice.lower() == "bank":
        bank()

    elif choice.lower() == "pawn shop":
        pawn_shop()

    elif choice.lower() == "bakery":
        bakery()

    elif choice.lower() == "bank" or "wallet" or "inventory":
        statcheck(choice, wallet, inventory, input_file_1)

    elif choice.lower() == "back" or "leave" or "start":
        start()

    else:
        city_centre()

def bank():
    global wallet

    while True:
        print("Welcome to the bank, would you like to DEPOSIT or WITHDRAW or go BACK?")
        choice = input("> ")

        if choice.lower() == "deposit":
            bank_deposit(wallet)

        elif choice.lower() == "withdraw":
            bank_withdraw()

        elif choice.lower() == 'back' or 'city' or 'city centre':
            city_centre()

        elif choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice, wallet, inventory, input_file_1)

        else:
            print("I'm sorry i don't understand that...")


def bank_deposit(wallet):

    while True:
        print(f"You have {wallet} in your wallet, how much would you like to deposit? Press ENTER to leave")
        deposit = input("> ")
        if deposit.isnumeric():

            deposit_int = int(deposit)

            if wallet - deposit_int < 0:
                print("Im sorry, you don't have enough funds...")

            elif wallet - deposit_int >= 0:
                contents = input_file_1.read()

                new_balance = contents + deposit
                converted_new_balance = str(new_balance)

                wallet -= deposit_int

                input_file_1.write(converted_new_balance)
                print(f"Thank you for depositing {deposit} gold or silver or whatever.")

                return wallet

            else:
                break
        else:
            break


def bank_withdraw():
    global wallet

    while True:
        input_file_1.seek(0)
        contents = input_file_1.read()
        print(contents)
        print(f"You have {contents} in your bank, how much would you like to withdraw?")
        withdraw = input("> ")
        if withdraw.isnumeric():

            withdraw_int = int(withdraw)
            contents_int = int(contents)
            if contents_int - withdraw_int < 0:
                print("Im sorry, you don't have enough funds...")

            elif contents_int - withdraw_int >= 0:
                print("contents", contents_int)
                print("withdraw", withdraw_int)
                new_balance = contents_int - withdraw_int
                print("new balance", new_balance)
                converted_new_balance = str(new_balance)

                wallet += withdraw_int
                input_file_1.seek(0)
                input_file_1.write(converted_new_balance)
                print(f"Thank you for withdrawing {withdraw} gold or silver or whatever."
                      f"You have {wallet} in your wallet")


            else:
                bank()
        else:
            bank()

bank()