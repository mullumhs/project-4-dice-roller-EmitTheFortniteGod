"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                DICE GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("*"*50)
print(" \n \n \n")
print("-"* 18, "Dice roller", "-"* 19)
print(" \n \n \n")
print("*"*50)


import random

#function 4 dice


def roll(qty, sides):
    for i in range(qty):
        roll = random.randint (sides)
        return roll


qty = int(input(print("how many dice do u want to roll: ")))
sides = int (input(print("how many sides would u like this dice to have: ")))



roll(qty, sides)






 



