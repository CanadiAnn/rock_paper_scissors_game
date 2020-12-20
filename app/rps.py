import random

rps = ["rock", "paper", "scissors"]

player1 = "scissors"
player2 = random.choice(rps)  #machine

# print("Player 1:", player1)
# print("Player 2:", player2)


if player1 == player2:
    print("Null")
elif player1 == "paper" and player2 == "rock":
    print("Paper covers rock: You win!")
elif player1 == "rock" and player2 == "paper":
    print("Paper covers rock: You lose!")
elif player1 == "scissors" and player2 == "rock":
    print("Rock crushes scissors: You lose!")
elif player1 == "rock" and player2 == "scissors":
    print("Rock crushes scissors: You win!")    
elif player1 == "paper" and player2 == "scissors":
    print("Scissors cuts paper: You lose!")
elif player1 == "scissors" and player2 == "paper":
    print("Scissors cuts paper: You win!")
