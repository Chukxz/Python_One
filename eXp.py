names = [
    "John",
    "Tobias",
    "Rhanerys",
    "Voldermort",
    "Megatron",
    "Optimus",
    "Daenerys",
    "Snow",
    "Cinderella",
    "Hobbit",
    "Copernicium"
]

#List Comprehension.
listName = [len(name) for name in names]

#Dictionary Comprehension.

dicName = {name:len(name) for name in names}

print(names)

print(listName)

print(dicName)