import random

def rollDice(sides):
    roll = random.randint(1, sides)
    print("You rolled ", roll)

rollDice(20)