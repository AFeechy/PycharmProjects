formatter = "{} {} {} {}"            #establishes formatter variable
print(formatter.format(1, 2, 3, 4))   # .format calls on format function and then    ,   ,   ,  ,  provides info
print(formatter.format("one", "two", "three", "four"))   # "strings" placed in {}
print(formatter.format(True, False, False, True)) #Boolean placed into {}
print(formatter.format(formatter, formatter, formatter, formatter)) #formatter variable placed into {}
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
  "Or a song about fear" ))