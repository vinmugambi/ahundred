import random, os, time

def characterHealth(): 
    return (rollDice(6) * rollDice(12) / 2) + 10

def characterStrength(): 
    return (rollDice(6) * rollDice(8) / 2) + 12

def rollDice(sides):
    return random.randint(1, sides)

while True:
    name = input("Name a GOT character: ")
    house = input("What's their house? ")
    strength = characterStrength()
    health = characterHealth()
    print(f"""
         {name} of house {house}
         health: {health}
         strength: {strength}
    """)
    playAgain = input("Play again? (Yes, No): ")
    while playAgain != "No" and playAgain != "Yes": 
       playAgain = input("Play again? Enter Yes or No: ")
    if playAgain == "No" : break
    elif playAgain == "Yes": 
        time.sleep(1)
        os.system("clear")
        continue
