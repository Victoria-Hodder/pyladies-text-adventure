import random
import time

def wrong_input(valid):
    print(f"\nSorry but the only valid options are: {valid}. \n")

def dead(means_of_death):
    print(f"Oops you died of {means_of_death}. Hope you had a nice life!")

    print("You are falling for...")
    for i in range(11):
        print(i)
        time.sleep(0.3)
    
    print("...meters")
    print("The game is finished")

friends = ["Frieda", "Nannie", "Michael", "Alan"]

door_greetings = {"1": "Welcome to the coffin room", "2": "Welcome to the treasure house", "3": "Welcome to the fun place!"}

print()
name = input("What is your name? ")
print(f"Welcome to the dungeon, {name}!")

door = 0

while door not in ("1", "2", "3"):
    if door != 0:
        wrong_input("1, 2")
    print("Do you go through door 1, door 2 or door 3?")
    door = input("> ") # anything you input here will be a string
    

if door == "1":
    print(f"{door_greetings[door]}") 
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    while vampire not in {"1", "2"}:
        wrong_input("1, 2")
        print("I'll ask again: do you choose 1 or 2?")
        vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")
        print("What is your favorite color?")
        favorite_color = input("> ")
        print(f"Amazing {name}, {favorite_color} is my best color too!")

    elif vampire == "2":
        print(f"Oh no {name}! The vampire is faster than you")
        dead("vampire bite")
    else:
        wrong_input("1, 2")

elif door == "2":
    print(f"{door_greetings[door]}") 
    print("On a beautiful table, there is a golden chalice with a red liquid inside")

    print("What do you do?")
    print("1. Drink it")
    print("2. Throw it on the floor")

    chalice = input("> ")

    if chalice == "1":
        dead("poison")    
    elif chalice == "2":
        print(f"Excellent idea {name}, you have avoided death")
    else:
        wrong_input("1, 2")

elif door == "3":
    print(f"{door_greetings[door]}") 
    rand_int = random.randint(0,3)
    print(f"And look, your friend {friends[rand_int]} is here.")
    print("They want to rescue you from this place")

    print("Is that OK? Please answer Y or N")

    is_OK = input("> ")

    if is_OK == "Y":
        print(f"Supi! Let's go {name}")
    elif is_OK == "N":
        print("Too bad, you will die alone")
        dead("loneliness")
    else:
        wrong_input("Y, N")

print()
bye = input("Say 'Good bye' in a language other than English: ")
print(f"{bye}, {name}!")