from sys import argv

script, bank_file = argv


def statcheck(inp, wallet, inventory, bank_file):
    if "wallet" in inp:
        print(wallet)

    elif "inventory" or "i" in inp:
        print(i)

    elif "bank" in inp:
        balance = (open(bank_file, 'r'))
        print(balance)

i = input(">")

wallet = 5

inventory = ["thing 2", "thing 3", "thing 4"]

if "wallet" or "inventory" or "bank" in i:
    statcheck(i, wallet, inventory, bank_file)