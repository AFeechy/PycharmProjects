from sys import argv

script, argv1, argv2 = argv


def distance(s, t):
    distance_travelled = s * t
    print(f'Miles travelled: {distance_travelled}')
    distance_to_moon = 238855 - distance_travelled
    print(f"If you drove to space you would be {distance_to_moon} miles far from the moon")


print('1st')
distance(30, 0.5)

print('2nd')
speed = int(input('Speed?: \n \t'))
distance(speed, 0.5)

print('3rd')
favourite_colour = len(input('What is your favourite colour?: \n\t '))
time = int(input('How long have you been sleeping?: \n\t '))
speed = favourite_colour * time
distance(speed, time)

print('4th')

distance(int(argv1), float(argv2))

print('5th')
distance(13 * 5, 10 * 2)

print('6th')
time = float(input('Time?: '))
speed = 60
distance(speed / 2, time * 5)

print('7th')
ans = input('Would you like to use my program? (Y to continue, other to quit): ')
if ans.upper() == 'Y':
    speed = int(input('Speed?: \n \t'))
    distance(speed, float(argv2))
else:
    quit()
