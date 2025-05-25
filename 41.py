character = {
    "name": "Ian",
    "health": 240,
    "strength": 199,
    "equipped": None
}

for value in character.values():
    print(value)

for name, value in character.items():
    print(f'{name}: {value}')

    if(name == "strength"):
        if(value>100):
            print("Whoa, soo strong")