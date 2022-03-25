weight = int(input('Weight: '))
unit = input('(L)bs or (K)gs: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} Kgs")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")