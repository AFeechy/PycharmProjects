def statcheck(input, wallet, inventory, bank_file):
    if "wallet" in input:
        print(wallet)

    elif "inventory" in input:
        print(inventory)

    elif "bank" in input:
        balance = (open(bank_file, 'r'))
        print(balance)
