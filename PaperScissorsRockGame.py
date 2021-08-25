import random

list = ["paper", "rock", "scissors"]
AI_choice = random.choice(list)
while True:

    User_Choice = input("paper, rock or scissors? ").lower()

    print(f"Okay so User choose {User_Choice} and the AI choose {AI_choice} ")

    if User_Choice == AI_choice:
        print("It's a draw")
    elif User_Choice == "rock":
        if AI_choice == "scissors":
            print("User won!")
        else:
            print("AI Won")
    elif User_Choice == "scissors":
        if AI_choice == "Rock":
            print("User won!")
        else:
            print("AI Won")
    elif User_Choice == "paper":
        if AI_choice == "rock":
            print("User Won")
        else:
            print("AI won")
    play_again = input("Wanna play again? (Y)es/(N)o ").upper()
    if play_again != "Y":
        break
