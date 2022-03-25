import time

inventory = ["Red Rock", "Grey Rock", "White Rock"]

global wallet

wallet = 0


def pawn_shop_sell():

    while True:

        global wallet

        print("What would you like to sell ? ")
        print(f"Inventory: {inventory}. Wallet: {wallet}")
        choice = input("> ")
        choice_t = choice.title()

        if choice_t in inventory:
            inventory.remove(choice_t)

            if choice_t == "Red Rock":
                wallet += 1
                print("You have sold a red rock for 1 rusty coin")
                time.sleep(1)

            elif choice_t == "Grey Rock":
                wallet += 1
                print("You have sold a red rock for 1 fresh'ish' cucumber")
                time.sleep(1)

            elif choice_t == "White Rock":
                wallet += 5
                print("You have sold a red rock for 5 golden rings")
                time.sleep(1)

        elif choice not in inventory:
            print(f"Sorry you don't appear to have any {choice} in your bag ")

        else:
            break



pawn_shop_sell()