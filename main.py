import random

def initialize_losses():
    # This initializes the losses for each player
    losses = {"Player 1": 0, "Player 2": 0, "Computer": 0}
    return losses

def get_valid_sticks():
    # Prompting the user to put in a valid input
    sticks = input("Please enter the number of sticks you want to take from the pile (between 10 and 100): ")
    # Error checking to tell the user to enter a valid input
    while not sticks.isdigit() or int(sticks) < 10 or int(sticks) > 100:
        print("Please enter a valid amount of sticks (between 10 and 100).")
        sticks = input("Please enter the number of sticks you want to take from the pile (between 10 and 100): ")
    return int(sticks)  # Return as an integer

def computer_choice():
    # Computer choosing sticks between 1 and 3
    choice = random.randint(1, 3)
    return choice

def player_choice(player_name):
    # Player makes a move
    move = input(f"{player_name}, how many sticks do you want to take? (1, 2, or 3): ")
    while not move.isdigit() or int(move) < 1 or int(move) > 3:
        print("Please enter a valid amount of sticks (1, 2, or 3).")
        move = input(f"{player_name}, how many sticks do you want to take? (1, 2, or 3): ")
    return int(move)  # Return as an integer

def main(sticks, losses):
    play_again = "yes"

    while play_again == "yes":
        print(f"Starting with {sticks} sticks.")

        while sticks > 0:
            p1_move = player_choice("Player 1")
            sticks -= p1_move
            print(f"Sticks remaining: {sticks}")
            if sticks <= 0:
                print("Player 1 is the loser, they took the last stick.")
                losses["Player 1"] += 1
                break

            p2_move = player_choice("Player 2")
            sticks -= p2_move
            print(f"Sticks remaining: {sticks}")
            if sticks <= 0:
                print("Player 2 is the loser, they took the last stick.")
                losses["Player 2"] += 1
                break

            computer_move = computer_choice()
            sticks -= computer_move
            print(f"Sticks remaining: {sticks}")
            if sticks <= 0:
                print("The computer took the last stick, it is the loser.")
                losses["Computer"] += 1
                break

        # After each game, ask if the user wants to play again
        play_again = input("Do you want to play again? Yes/No: ").lower()

    return losses

def play_game():
    losses = initialize_losses()

    print("Welcome to the Stick Game!")

    # Set initial stick count
    sticks = get_valid_sticks()

    # Play the game, keep updating losses across rounds
    losses = main(sticks, losses)

    # Print final results after the user chooses to stop
    print("Game over. Here are all the total losses:")
    print(losses)

# Run the game
play_game()












