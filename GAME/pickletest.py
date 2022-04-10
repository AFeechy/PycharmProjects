import pickle
colours = {"Red": ["Dark Red", "Pink"] ,
           "Blue": ["Light Blue", "Azul"]}   # list can be used within dictionary as can other data type, boolean, float ect.

with open('colour.pickle', 'wb') as pickleFile:       # wb is write as binary
    pickle.dump(colours, pickleFile, protocol=pickle.HIGHEST_PROTOCOL)

with open('colour.pickle', 'rb') as pickleFile:
    loadedFile = pickle.load(pickleFile)

print(colours == loadedFile)
