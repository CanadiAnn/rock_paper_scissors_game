import random

rps = ["rock", "paper", "scissors"]

player1 = "scissors"
player2 = random.choice(rps)

print("Player 1:", player1)
print("Player 2:", player2)


if player1 == player2:
    print("Null")
elif player1 == "paper" and player2 == "rock":
    print("Paper surrounds the rock: Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("Paper surrounds the rock: Player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Rock breaks the scissors: Player 2 wins!")
elif player1 == "rock" and player2 == "scissors":
    print("Rock breaks the scissors: Player 1 wins!")    
elif player1 == "paper" and player2 == "scissors":
    print("Scissors cut the paper: Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Scissors cut the paper: Player 1 wins!")
