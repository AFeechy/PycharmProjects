from sys import argv    # imports command line arguments to script. argv[0] is script name
# read the WYSS section for how to run this
script, first, second, third, fourth = argv

print(f'''
          The script it called:, {script}
          Your first variable is: {first}
          Your second variable is: {second}
          Your third variable is: {third}
''')

name = input("What is your name? ")
print(f'And your name is {name} {fourth}')
