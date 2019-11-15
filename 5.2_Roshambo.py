'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
win = 0
loss = 0
done = False

print("Welcome to Peggy's Roshambo Program!")
while not done:
    computer = random.randrange(1, 4)
    player = int(input("\n 1 for Rock \n 2 for Paper \n 3 for Scissors \n 4 to Quit"))
    if player == computer:
        print("Tied!")
    elif player == 1:
        if computer == 2:
            print("You lose! Paper covers rock.")
            loss += 1
        else:
            print("You win! Rock beats scissors.")
            win += 1
    elif player == 2:
        if computer == 1:
            print("You win! Paper covers rock.")
            win += 1
        else:
            print("You lose! Scissors cut paper.")
            loss += 1
    elif player == 3:
        if computer == 1:
            print("You lose! Rock beats scissors.")
            loss += 1
        else:
            print("You win! Scissors cut paper.")
            win += 1
    elif player == 4:
        done = True
    else:
        print("Invalid choice, please try again. \n Remember to type the numbers.")

print("Your final win/loss ratio is:", win, "/", loss)





