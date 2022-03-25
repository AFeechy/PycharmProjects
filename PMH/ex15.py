from sys import argv               # sys module to import info or arguments (argv) from command line

script, filename = argv            # script imports script name (ex15.py) filename provided in cmd line (ex15_sample.txt)

txt = open(filename)               # sets variable to open file

print(f"Here's your file {filename} :")   # format line shows filename and .read specifies how to bhave when printing
print(txt.read(99))

print("Type the filename again:")
file_again = input("> ")          # sets variable to input

txt_again = open(file_again)     # sets variable to open previous variable

print(txt_again.read())
txt.close()
txt_again.close()