"""
Rock Paper and Sccissors
rock beats scissors, scissors beats paper and paper beats rock
"""

from getpass import getpass as input  # hide user input

# collect player picks
print("Select your move: R, P, S")
player1 = input("Player 1: ")
player2 = input("Player 2: ")

# you loose if you choose an invalid character
validPicks = ["P", "R", "S"]
if player1 not in validPicks:
    print("Player 2 wins")
elif player2 not in validPicks:
    print("Player 1 wins")

# draw if both pick same item
elif player1 == player2:
    print("oops! draw. you all picked", player1, "wanna try again?")

# player 1 winning conditions
elif (
    (player1 == "R" and player2 == "S")
    or (player1 == "S" and player2 == "P")
    or (player1 == "P" and player2 == "R")
):
    print("Player 1 has won.", player1, "beats", player2)

# zero sum, player 1 not winning means player 2 has won.
else:
    print("player2 has won.", player2, "beats", player1)
