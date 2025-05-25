# String manupulation

name = input("O na na. What's your name?\n")

if name.lower().strip() == "david":
    print("Hello baldy!")
else: 
    print("What a beautiful head of hair")



myList = []

def printList():
    print()
    for i in myList:
        print(i)
    print()


while True:
    addItem = input("Item > ").strip().capitalize()
    if addItem not in myList:
        myList.append(addItem)
    printList()
    
