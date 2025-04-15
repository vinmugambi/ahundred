import random

def rollDice(sides):
    return random.randint(1, sides)

input("name your character? ")

def characterStatGenerator():
   return rollDice(6) * rollDice(8)

health = characterStatGenerator()
print("Their health is", health)