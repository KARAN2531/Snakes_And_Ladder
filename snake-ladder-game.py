import random

#UC1 - Snake and Ladder game played with single player at start position 0
user_position = 0
comp_position = 0
user_dice_count = 0
comp_dice_count = 0

#UC2 - The Player rolls the die to get a number between 1 to 6.
def roll_dice():
    return random.randint(1,6)

#UC3 - The Player then checks for a option. They are No Play, Ladder or Snake.
def check_movement():
    lst = ["No Play", "Ladder", "Snake"]
    return random.choice(lst)

#UC4 - Repeat till the Player reacher the winning poistion 100. 
def gameover():
   return comp_position == 100 or user_position == 100