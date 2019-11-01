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
    comp_c = random.randrange(1, 4)
    user_c = input("1 for Rock \n 2 for Paper \n 3 for Scissors \n 4 to Quit")
    if user_c == comp_c:
        print("Tied!")



#     if user_c == comp_c:
#         print("Tied")
#     elif user_c !=
#     else:
#         print("Invalid choice. Please try again.")
#         continue
#
#     if
#
# print()







