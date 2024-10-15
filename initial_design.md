# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully
# Start the Game

initialize variables

losses["Player 1"] = 0

losses["Player 2"] = 0

losses["Player 3 (Computer)"] = 0
2. Main Game Loop (Repeat for Each Match):
Set the Initial Count of Sticks:
Prompt the user to enter a number of sticks that is valid, ranging from 10 to 100.  
Validate that the input is an integer.
If it is not, continue to ask until a correct value is provided.
Determine the Starting Player:
Assign current_player to "Player 1", indicating that Player 1 will take the first turn.
3. Continue Playing Until the Game Concludes (while sticks are remaining):
Show the Sticks Left:
Inform the players about the number of sticks currently available on the table.
Player's Turn:
For Player 1 and Player 2:

Ask the current player how many sticks they wish to take (1, 2, or 3).  
Check the input for validity. If it's not valid (either not an integer or not between 1 and 3), keep prompting until they provide a valid choice.  
For Player 3 (Computer):

The computer will randomly choose either 1, 2, or 3 sticks.  
Display the number of sticks the computer has taken.  
Update the Total Count of Sticks:  
Reduce the total number of sticks by the amount chosen by the player or computer.  
Check for Game Conclusion:  
If the remaining number of sticks equals 0:  
The current player loses since they took the last stick.  
Increment the loss count for that player using losses[current_player] += 1.  
Exit the current game loop and proceed to the next step.  
Rotate Players (If the Game is Still Active):  
If current_player is "Player 1", change it to "Player 2".  
If current_player is "Player 2", switch to "Player 3 (Computer)".  
If current_player is "Player 3 (Computer)", revert to "Player 1". 
4. After the Game Concludes:
Ask If the User Wants to Continue Playing:
If the user responds with "yes," restart the game by returning to step 2 (reset the number of sticks and keep tracking losses).  
If the user responds with "no," move to the final step.
5. Conclude the Session:  
Show the Loss Statistics:  
Display how many losses each player has accumulated:  
print("Player 1:", losses["Player 1"], "losses"). 
print("Player 2:", losses["Player 2"], "losses"). 
print("Player 3 (Computer):", losses["Player 3 (Computer)"], "losses").  
End the game.   
6. Important Considerations:  
Input Validation: Ensure that all user inputs are acceptable (the initial count of sticks must be between 10 and 100; the number of sticks taken must be 1, 2, or 3).  
Player Turn Sequence: Ensure players take turns in the proper order: Player 1, then Player 2, followed by Player 3 (Computer).  
Tracking Losses: Keep count of how many losses each player has and present this information after the user decides to stop playing.   
7. Sample Game Flow:  
Initial Setup: The user enters 20 sticks.  
Turn 1: Player 1 removes 2 sticks (remaining sticks: 18).  
Turn 2: Player 2 removes 1 stick (remaining sticks: 17).  
Turn 3: The computer takes 3 sticks (remaining sticks: 14).  
The game continues until all sticks are taken.  
The player who removes the last stick loses the game.  
Ask if the players wish to play another round. If they choose "yes," restart the game; if they choose "no," show the total losses.  
