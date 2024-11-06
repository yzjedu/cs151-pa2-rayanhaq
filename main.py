import random



def initialize_losses():
    #This initializes the losses for each player
    losses = {"Player 1":0, "Player 2":0, "Computer":0}
    return losses

def get_valid_sticks():
    #prompting the user to put in a valid input
    sticks = input("please enter the amount of sticks you want to take from the pile {10,100}")
    #Error checking to tell the user to enter a valid input
    while not sticks.isdigit() or not (10 <= int(sticcks) <= 100):
        print("Please enter a valid number of sticks (between 10 and 100).")
        sticks = input("Please enter the amount of sticks you want to start with (between 10 and 100): ")
    return int(sticks)


def computer_choice():
    #Computer choosing sticks between 1 and 3
    choice = random.randint(1, 3)
    return choice

def player_choice(player_name):
    move = int(input(f"{player_name}How many sticks do you want to take?"))
    while not move.isdigit() or int(move) < 1 or int(move) > 3:
        print("Please enter a valid number of sticks (1, 2, or 3).")
        move = input(f", {player_name}how many sticks do you want to take (1, 2, or 3)? ")
    return int(move)

def main(sticks, losses):


        while sticks > 0:
            p1_move = player_choice("Player 1")
            sticks -= p1_move
            print(f"Sticks remaining: {sticks}")
            if sticks <= 0:
                print("Player 1 is the loser, he took the last stick")
                losses["Player 1"] += 1
                break  # The inner while loop ends here and continues to the next round

            p2_move = player_choice("Player 2")
            sticks -= p2_move
            print(f"Sticks remaining: {sticks}")
            if sticks <= 0:
                print("Player 2 is the loser, he took the last sticks")
                losses["Player 2"] += 1
                break  # The inner while loop ends here and continues to the next round

            computer_move = computer_choice()
            sticks -= computer_move
            print(f"Sticks remaining: {sticks}")
            if sticks <= 0:
                print("The computer took the last sticks, he is the loser")
                losses["Computer"] += 1
                break  # The inner while loop ends here and continues to the next round

        # Ask if the user wants to play again
        ##play_again = input("Do you want to play again? Yes/No").lower()

        return sticks



def play_game():
    losses = initialize_losses()

    play_again = "yes"

    while play_again == "yes":
        sticks = get_valid_sticks()
        print(f"starting with {sticks} sticks")
        main(sticks, losses)

        play_again = input("Do you want to play again? Yes/No")

    print("Game over. Here are all the total losses:")
    print(losses)

play_game()











