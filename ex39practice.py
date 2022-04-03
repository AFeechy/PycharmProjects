county = {
    'Northamptonshire': 'Northants',
    'Cambridgeshire': 'Cambs',
    'Leictershire': 'Leics',
    'Suffolk': 'Suff'
}

town = {
    'Northants': 'Northampton',
    'Cambs': 'Cambridge',
    'Leics': 'Leicester',
    'Suff': 'Ipswich'
}

print(county)

print(town)

print('Which county would you like to add to the database?')
new_county = input('>')
print('What is the abbreviation of the county?')
new_abbrev = input('>')
print('What is the biggest town in the county?')
new_town = input('>')

county[new_county] = new_abbrev
town[new_abbrev] = new_town

print(county)
print(town)