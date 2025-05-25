myAgenda = []

def printList():
   print()
   for item in myAgenda:
      print(item)
   print()

while True:
    item = input("What's next on the Agenda? ")
    if (item != "nothing"): 
      myAgenda.append(item)
      printList()
    else: break
