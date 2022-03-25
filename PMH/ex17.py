from sys import argv      # imports arguments from command line

from os.path import exists     # imports exists boolean status

script, from_file, to_file = argv        # arguments set0

print(f"Copying from {from_file} to {to_file}")

# we could do these next two on one line, how?       # with ';' to seperate on same line code

in_file = open(from_file)    # sets infile variable as opened file ( from_file variable imported from arguments)
indata = in_file.read()  # sets indata variable as text from from_file

print(f"The input file is {len(indata)} bytes long") # prints formatted string with len (len provides number for amount of characters or bytes)

print(f"Does the output file exist {exists(to_file)}")
print("Ready, hit RETURN to contiue, CTRL - C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")


in_file.close()