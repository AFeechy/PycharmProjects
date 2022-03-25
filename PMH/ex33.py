def while_1(x, count, number, increase):
    while x < count:
        print(f"At the top i is {x}.")
        number.append(x)

        x += increase
        print("Numbers now: ", number)
        print(f"At the bottom i is {x}")


i = 10
count_limit = 30
numbers = []
inc_amount = 2

#while_1(i, count_limit, numbers, inc_amount)

#print("The numbers: ")

#for num in numbers:
    #print(num, end=' ')


def for_1(a, b, c, numbers):
    for x in range(a, b, c):
        print(f"At the top is {x}.")
        numbers.append(x)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {x}")

numbers = []

for_1(5, 30, 5, numbers)
