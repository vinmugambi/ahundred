# Number guessing game

raffle = 63
prize: int = 100
tries = 0

input(
    "A magic number between 1 and 100, will win you a 100 shillings. The prize will decrease with the number of tries. Press enter to play. "
)

while True:
    pick = int(input("What is the magic number? "))
    tries = tries + 1
    prize = prize / tries
    if pick == raffle:
        print("Correct! you got it in", tries, "You have won", prize, "shillings")
        break
    else:
        continue
