import random
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


list = ["paper", "rock", "scissors"]

while True:

    IA_choice = random.choice(list)
    User_Choice = input("paper, rock or scissors? ").lower()

    print(f"Okay so User choose {User_Choice} and the IA choose {IA_choice} ")

    if User_Choice == IA_choice:
        print("It's a draw")
    elif User_Choice == "rock":
        if IA_choice == "scissors":
            print("User won!")
        else:
            print("IA Won")
    elif User_Choice == "scissors":
        if IA_choice == "Rock":
            print("User won!")
        else:
            print("IA Won")
    elif User_Choice == "paper":
        if IA_choice == "rock":
            print("User Won")
        else:
            print("IA won")
    play_again = input("Wanna play again? (Y)es/(N)o ").upper()
    if play_again != "Y":
        break
