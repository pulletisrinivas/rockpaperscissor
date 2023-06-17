import random

# Define the possible moves.
moves = ["rock", "paper", "scissors"]

# Get the user's move.
user_move = input("Enter your move (rock, paper, or scissors): ")

# Get the computer's move.
computer_move = random.choice(moves)

# Display the moves.
print("You chose:", user_move)
print("Computer chose:", computer_move)

# Determine the winner.
if user_move == computer_move:
    print("Tie!")
elif user_move == "rock":
    if computer_move == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_move == "paper":
    if computer_move == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_move == "scissors":
    if computer_move == "paper":
        print("You win!")
    else:
        print("Computer wins!")