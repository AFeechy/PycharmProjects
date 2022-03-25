from sys import argv

script, filename = argv

txt = open(filename)
print(txt.read())

print(f"We're going to erase {filename}.")
print("If you don't want to do that, press N")
print("If you do want to do that, press Y")

ans = input("?")
if ans.upper() == 'Y':
    print("Opening the file...")
    target = open(filename, 'w')   # w = write   r = read (default)   a = append

    print("Truncating the file. Goodbye!")  # not necessary with w mode
    target.truncate()

    print("Now I am going to ask you for three lines.")

    line1 = input("Line 1: ")
    line2 = input("Line 2: ")
    line3 = input("Line 3: ")

    print("I'm going to write these to the file.")

    target.write(f"{line1} \n{line2} \n{line3}")

    print("And finally, we close the file.")
    target.close()
elif ans.upper() == 'N':
    txt.close()
    print("Goodbye !")
