import random

nameList = ["Vincent", "Mugambi", "Wambui"]

nameList[0] = "Just"
nameList.remove("Wambui")

for name in nameList:
    print(name)

print('lastname is ', nameList[-1]) # last name


greetings = ["Hello", "Habari", "Wimwega", "Nesa"]

def randomGreeeting():
    position = random.randint(0, greetings.__len__() - 1)
    print(f'Greeting {position + 1} is {greetings[position]}')

randomGreeeting()



