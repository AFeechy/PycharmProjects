from sys import argv ; from os.path import exists ; script, from_file, to_file = argv  # imports arguments from command line, imports exists boolean status, arguments set

indata = open(from_file).read()           # sets indata variable as open read from_file

print(f"exists from? {exists(from_file)} exist to? {exists(to_file)}") # prints boolean of file existing

open(to_file, 'w').write(indata)  # opens file in write mode 'w' writes indata variable ------ .read means no need to close
