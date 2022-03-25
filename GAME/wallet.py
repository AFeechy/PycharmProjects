from sys import argv


script, input_file_1 = argv

global wallet

wallet = 5


def bank_withdraw():
    global wallet

    while True:
        with open(input_file_1, 'r') as current_bank:
            contents = current_bank.read()

        print(f"You have {contents} in your bank, how much would you like to withdraw?")
        withdraw = input("> ")
        if withdraw.isnumeric():

            withdraw_int = int(withdraw)
            contents_int = int(contents)
            if contents_int - withdraw_int < 0:
                print("Im sorry, you don't have enough funds...")

            elif contents_int - withdraw_int >= 0:
                new_balance = int(contents) - withdraw_int
                converted_new_balance = str(new_balance)

                wallet += withdraw_int

                open(input_file_1, 'w').write(converted_new_balance)
                print(f"Thank you for withdrawing {withdraw} gold or silver or whatever."
                      f"You have {wallet} in your wallet")

            else:
                break
        else:
            break







def bank_deposit(wallet):
    while True:
        print(f"You have {wallet} in your wallet, how much would you like to deposit?")
        deposit = input("> ")
        if deposit.isnumeric():

            deposit_int = int(deposit)

            if wallet - deposit_int < 0:
                print("Im sorry, you don't have enough funds...")

            elif deposit_int > 0:
                with open(input_file_1, 'r') as current_bank:
                    contents = current_bank.read()

                new_balance = int(contents) + deposit_int
                converted_new_balance = str(new_balance)

                wallet -= deposit_int

                open(input_file_1, 'w').write(converted_new_balance)
                print(f"Thank you for depositing {deposit} gold or silver or whatever.")

            else:
                break
        else:
            break

bank_withdraw()