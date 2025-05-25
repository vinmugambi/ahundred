clue = {}

def prettyPrint():
    for key, value in clue.items():
        print(key, value)
    print()

while True:
    name = input("Character name: ")
    weapon = input("Character's weapon: ")

    clue[name] = {'weapon': weapon}
    prettyPrint()

