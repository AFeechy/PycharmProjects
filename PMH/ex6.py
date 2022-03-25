types_of_people = 15                 # variable
x = f"There are {types_of_people} types of people."  # formated string with 2 variables

binary = "binary"    # variable
do_not = "don't"  # variable
y = f"Those who know {binary} and those who {do_not}"

print(x)  # print variable x
print(y)  # print variable string y

print(f"I said: {x}")                     # print format string with inserted variable
print(f"I also said: '{y}'")               # print format string with inserted variable

hilarious = False                          # boolean
joke_evaluation = "Isn't that joke so funny?! {}"   # curly brackets mark point for .format to insert
print(f"{joke_evaluation} {hilarious}")            # .format(xxx) inserts


w = "This is the left side of..."
e = "a string with a right side."
print(w + e)