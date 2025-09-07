import random

option = ["rock", "paper", "scissors"]

while True:
    user = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower().strip()

    # quit early
    if user == "q":
        print("Thank you for playing")
        break

    # validate input
    if user not in option:
        print("I'm sorry, that's not a valid option")
        continue

    # play a round
    computer = random.choice(option)

    if computer == user:
        print("You and computer chose the same thing")
    elif computer == "rock" and user == "paper":
        print(f"Computer chose {computer} and you chose {user}, so you won!")
    elif computer == "rock" and user == "scissors":
        print(f"Computer chose {computer} and you chose {user}, so you lost!")
    elif computer == "paper" and user == "scissors":
        print(f"Computer chose {computer} and you chose {user}, so you won!")
    elif computer == "scissors" and user == "paper":
        print(f"Computer chose {computer} and you chose {user}, so you lost!")
    elif computer == "scissors" and user == "rock":
        print(f"Computer chose {computer} and you chose {user}, so you won!")
    elif computer == "paper" and user == "rock":
        print(f"Computer chose {computer} and you chose {user}, so you lost!")
