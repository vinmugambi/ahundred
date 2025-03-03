# continue - restart loop
# exit - stops the program

"""
Rock Paper and Scissors - multiple round
rock beats scissors, scissors beats paper and paper beats rock
"""

from getpass import getpass as input  # hide user input

print("Rock paper and Scissors ")
player1Score = 0
player2Score = 0

while True:
    # collect player picks
    print("Select your move: R, P, S")
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")

    # you loose if you choose an invalid character
    validPicks = ["P", "R", "S"]
    if player1 not in validPicks:
        player2Score = player2Score + 1
        print("Player 2 wins the round. Player 1 palayed an invalid move ", player1)
        if player2Score == 3:
            break
        else:
            continue
    elif player2 not in validPicks:
        player1Score = player1Score + 1
        print("Player 1 wins the round. Player 2 played an invalid move", player2)
        if player1Score == 3:
            break
        else:
            continue

    # draw if both pick same item
    elif player1 == player2:
        print("oops! draw. you all picked", player1)

    # player 1 winning conditions
    elif (
        (player1 == "R" and player2 == "S")
        or (player1 == "S" and player2 == "P")
        or (player1 == "P" and player2 == "R")
    ):
        player1Score = player1Score + 1
        print("Player 1 has won the round. ", player1, "beats", player2)
        if player1Score == 3:
            break
        else:
            continue
    # zero sum, player 1 not winning means player 2 has won.
    else:
        player2Score = player2Score + 1
        print("player2 has won thre round. ", player2, "beats", player1)
        if player2Score == 3:
            break
        else:
            continue
winner = (
    "Player 1" if player1Score == 3 else "Player 2" if player2Score == 3 else "No one"
)

print(winner, "has won the game")
