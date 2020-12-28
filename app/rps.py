import random

rps = ["rock", "paper", "scissors"]

player = "scissors"
computer = random.choice(rps)  #machine

# print("Player:", player)
# print("Computer:", computer)


if player == computer:
    print("Null")
elif player == "paper" and computer == "rock":
    print("Paper covers rock: You win!")
elif player == "rock" and computer == "paper":
    print("Paper covers rock: You lose!")
elif player == "scissors" and computer == "rock":
    print("Rock crushes scissors: You lose!")
elif player == "rock" and computer == "scissors":
    print("Rock crushes scissors: You win!")    
elif player == "paper" and computer == "scissors":
    print("Scissors cuts paper: You lose!")
elif player == "scissors" and computer == "paper":
    print("Scissors cuts paper: You win!")
