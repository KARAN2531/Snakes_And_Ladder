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

#UC 5 - Ensure the player gets to exact winning position 100.
def usermovement():
    global user_dice_count, user_position
    print("User move: ")
    x = roll_dice()
    y = check_movement()
    if y == "No Play":
        print(f"user stays at {user_position} ")
    elif y == "Ladder" and user_position + x <= 100:
        user_position = user_position + x
        print(f"user moves {x} steps ahead to {user_position} ")
    elif y == "Snake" and user_position - x >= 0:
        user_position = user_position - x  
        print(f"user moves {x} steps back to {user_position} ")
    elif user_position + x > 100 or user_position - x <0:
        print(f"User stays at {user_position}") 
    user_dice_count += 1      

def compmovement():
    global comp_dice_count, comp_position 
    print("Comp Move: ")
    x = roll_dice()
    y = check_movement()
    if y == "No Play":
        print(f"comp stays at {comp_position} ")
    elif y == "Ladder" and comp_position + x <= 100:
        comp_position = comp_position + x
        print(f"comp moves {x} steps ahead to {comp_position} ")
    elif y == "Snake" and comp_position - x >= 0:
        comp_position = comp_position - x
        print(f"comp moves {x} steps back to {comp_position} ")
    elif comp_position + x > 100 or comp_position - x < 0:    
        print(f"Comp stays at {comp_position}") 
    comp_dice_count += 1

#UC6 -  Report the number of times the dice was played to win the game and also the position after every die role. 
def play_game():
    print("Enter snakes and ladder")
    input("Press Enter to make a toss:")
    toss = random.randint(0,1)
    whoseturn = toss
    while not gameover():
        if whoseturn == 0:
            compmovement()
            print("\n")
        else:
            usermovement()
            print("\n")
        whoseturn = 1 - whoseturn   