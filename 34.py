import os, time

listOfEmail = []

def prettyPrint():
    os.system("clear")
    print("list of emails")
    print()
    for index in range(len(listOfEmail)):
        print(f'{index + 1}: {listOfEmail[index]}')
    time.sleep(1)

while True:
    print("SPAMMER Inc. ")
    menu = input("1: Add Email \n2: Remove Email \n3: Show emails \n4:Get SPAMMING \n")
    if(menu == "1"):
        email = input("email > ")
        listOfEmail.append(email)
    elif(menu == "2"):
        email = input("email > ")
        if(email in listOfEmail):
           listOfEmail.remove(email)
        else: print("Not in email list")
    elif(menu == "3"):
        prettyPrint()
    else:
         email = input("email > ")
         print("email has been sent")