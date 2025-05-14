import random, os, time

def characterHealth(): 
    return (rollDice(6) * rollDice(12) / 2) + 10

def characterStrength(): 
    return (rollDice(6) * rollDice(8) / 2) + 12

def rollDice(sides):
    return random.randint(1, sides)


character1 = name = input("Name you favorite dragon: ")
character1House = input("What's their house? ")
character1Strength = characterStrength()
character1Health = characterHealth()

character2 = name = input("Who are they battling? ")
character2House = input("What's their house? ")
character2Strength = characterStrength()
character2Health = characterHealth()

rounds = 0

while True:
    rounds = rounds + 1
    print("__ BATTLE TIME __")
    character1Score = rollDice(6)
    character2Score = rollDice(6)

    difference = character1Score - character2Score

    if (difference > 0):  
        print(character1, "takes the round", character1Score, "-"  ,character2Score)
        character2Health = character2Health - difference
    elif (difference < 0):
        print(character2, "takes the round", character1Score, "-" , character2Score)
        character1Health = character1Health + difference
    else:
        print("Draw")

    if(character1Health <= 0):
        print(character2, "wins in", rounds, "rounds")
        break
    elif(character2Health <= 0):
        print(character1, "wins in", rounds, "rounds")
        break
    else: 
        time.sleep(1)
        os.system("clear")
        continue
