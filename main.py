import random

#initialize losses
player1_losses= 0
player2_losses = 0
computer_losses = 0
play_again = "y"

# Initial prompt for the number of sticks
sticks = input("Enter the number of sticks to start with (between 10 and 100): ")

# Loop until valid input is provided
while play_again == "y":
    while not (sticks.isdigit() and 10 <= int(sticks) <= 100):
        print("Error: Please enter a valid number between 10 and 100.")
        sticks = input("Enter the number of sticks to start with (between 10 and 100): ")

    # Convert to integer after validation
    sticks = int(sticks)

    # Display the result
    print(f"The game will start with {sticks} sticks.")

    current_player = 1

    while sticks > 0:

        if current_player == 1:
            print("It is players 1's turn")
            user_input = input("Please take 1 - 3 sticks")
            while not (user_input.isdigit() or 1 <= int(user_input) <= 3):
                print("Error: Please enter a valid number between 1 and 3.")
                user_input = input("Please take 1 - 3 sticks")

            take = int(user_input)
            sticks -= take

            if sticks <= 0:
                print("Player 1 took the last stick and looses")
                player1_losses += 1
            current_player += 1

        elif current_player == 2:
            print(f"There are {sticks} sticks on the table")
            print("It is players 2's turn")
            user_input = input("Please take 1 - 3 sticks")
            while not (user_input.isdigit() or 1 <= int(user_input) <= 3):
                print("Error: Please enter a valid number between 1 and 3.")
                user_input = input("Please take 1 - 3 sticks")
            take = int(user_input)
            sticks -= take

            if sticks <= 0:
                print("Player 2 took the last stick and looses")
                player2_losses += 1
            current_player = "computer"

        elif current_player == "computer":
            user_input = random.randint(1, 3)
            print(f"The computer has taken {user_input} sticks")
            sticks -= take
            print(f"There are {sticks} sticks on the table")

            if sticks <= 0:
                print("Computer took the last stick and looses")
                computer_losses += 1
            current_player = 1

    play_again = input("Would you like to play again? (y/n): ").lower().strip()
    while play_again != "y":
        print(f"Player 1 losses: {player1_losses}")
        print(f"Player 2 losses: {player2_losses}")
        print(f"Computer losses: {computer_losses}")















