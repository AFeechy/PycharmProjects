print("How many cats do you own?", end=' ')
cats_owned = int(input())
if cats_owned == 0:
    print("I think you need a cat !")
elif cats_owned <= 2:
    print("A perfect amount of cats!")
elif cats_owned > 2:
    print("Congratulations you are a crazy cat lady!")