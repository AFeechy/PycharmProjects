tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\\\ a \\ cat."                  # backslash (\) opens escape sequences pg 35

fat_cat = """
Ill do a list:
\t* Cat Food   
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print(f"If you \nwant me to be then \n{tabby_cat}\n\t{backslash_cat}")
