name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_kg = weight * 0.453
height_cm = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
print(f"My weight converted to kg is {weight_kg}Kgs.")
print(f"My height converted to cm is {height_cm}cm.")
#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"If I convert to metric I am {height_cm}cm tall and {weight_kg} Kgs heavy.")