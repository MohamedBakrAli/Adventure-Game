import time
from os import system, name

#
# Prints the given message and sleep for 2 ms.
#
def print_pause(message):
    print(message)
   # time.sleep(2)

#
# Take a valid choice from the player.
# 
def enter_choice(choice_code_to_choice_map):
    player_input = str(input("Please enter your choice: "))
    # check the validation of the player input
    while player_input not in choice_code_to_choice_map:
        player_input = str(input("Invalid choice!\n"
                                 "Please enter your choice: "))

    return choice_code_to_choice_map[player_input]

#
# Prints the choices and takes the player choice
# and perfoms the player choice.
#
def player_choice(choices):
    print_pause("What do you want to do next?")

    # print the choices messages
    for choice in choices:
        print_pause(choice.code + ". " + choice.message)

    # build a map from the choice code to the choice object
    choice_code_to_choice_map = {c.code : c for c in choices}
    # take the player input choice
    player_choice = enter_choice(choice_code_to_choice_map)
    # perfom the player choice
    player_choice.perform()



#
# Clears the screen
#
def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')