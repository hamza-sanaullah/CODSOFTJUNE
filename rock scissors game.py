import random

comp_turn = ["r", "s", "p"]
options = {
    "r": "rock",
    "s": "scissors",
    "p": "paper"
}

while True:  # Loop to keep playing until the user quits
    comp_choice = random.choice(comp_turn)

    user_choice = input("Choose rock(r), paper(p), or scissors(s) (or type 'q' to exit):\n").lower()

    if user_choice == 'q':
        print("Exiting the game.")
        break  # Exit the loop if the user chooses to quit
    elif user_choice in options:
        print(f"You chose {options[user_choice]}")
    else:
        print("Invalid choice. Please choose r, p, or s.")
        continue  # Skip the rest of the loop and start over

    print(f"Computer chose {options[comp_choice]}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif user_choice == "r":
        if comp_choice == "s":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "s":
        if comp_choice == "p":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "p":
        if comp_choice == "r":
            print("You win!")
        else:
            print("Computer wins!")
