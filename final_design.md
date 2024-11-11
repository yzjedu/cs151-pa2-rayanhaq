1. Initialize variables
- player1_losses = 0
- player2_losses = 0
- computer_losses = 0
- play_again = y

2. Create a prompt asking the user to take a number of sticks between 10 and 100
3. Create a loop while play_again = y
- Check of the input for number of sticks is not a digit or between 10 and 100
    1. print a error message
  2. ask user for a re prompt
- convert sticks to a integer after
4. display results and set current player to 1
5. while sticks > 0
- ask player 1 to take between 1-3 sticks
    1. if not digit or not between restrictions ask for a reprompt
- subtract the amount they took from the total amount
- if sticks <= 0
    1. output player 1 looses
  2. update player 1 total losses
- add 1 to current player

- ask player 2 to take between 1-3 sticks
    1. if not digit or not between restrictions ask for a reprompt
- subtract the amount they took from the total amount
- if sticks <= 0
    1. output player 2 looses
  2. update player 2 total losses
- set current_player to computer
- computers choice is random int between 1 and 3
- print the amount they take
- subtract the sticks from the total amount
- 1.- if sticks <= 0
    1. output computer looses
  2. update computer total losses
- set current player to 1

1. ask the user if they want to play again
- if not print all the total losses



