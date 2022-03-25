from sys import argv
script = argv

print("""
         Hello, and welcome to Alex's Leg Spreader
                The premium file opener.
        Please enter the name of the file you would like to open:
""")
file = input("> ")
print("Opening file to read...")
txt = open(file)

print(txt.read())

print("Press enter 'D' when you are finsihed.")
rtn = input(">")
if rtn == 'D':
    txt.close()
    print("Thanks for using Alex's leg spreader.")
else:
    print("Sorry i didnt understand that")










#print("Are you finished with the file ? (Y/N)")
#ans = input("> ")
#if ans.upper() == "Y":
#    txt.close()
#    print("Thanks for using Alex's file spreader.")
#elif ans.upper() == "N":
