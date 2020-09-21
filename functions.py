from sys import exit  # exit builtin function is used to terminate the program

# start room
def start():

    choice = input("There is a door to your right and left."
                   "Which one do you take? ")

    if choice == "left":
        bank_room()
    elif choice == "right":
        your_room()  # you need to create the function your_room
    else:
        dead("You stumble around the room until you starve.")


def your_room():

    choice = input("This room is full of sweets. "
                   "How many bags do you take? ")

    if choice.isdigit():

        if int(choice) > 0 and int(choice) < 50:
            print("That is a healthy amount!")
            exit(0)
        elif int(choice) > 50:
            dead("Phew you have a sweet tooth")

    else:
        dead("Man, learn to type a number.")

# second room
def bank_room():

    choice = input("This room is full of money."
                   "How many bank note bundles do you take? ")

    if choice.isdigit():

        if int(choice) > 0 and int(choice) < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        elif int(choice) > 50:
            dead("You greedy bastard!")

    else:
        dead("Man, learn to type a number.")

def dead(message):
    print(message, "You are dead.")
    exit(0)

start()