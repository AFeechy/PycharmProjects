from sys import argv

script, bank_file = argv




i = input(">")

wallet = 5

inventory = ["thing 2", "thing 3", "thing 4"]

if "wallet" or "inventory" or "bank" in i:
    statcheck(i, wallet, inventory, bank_file)