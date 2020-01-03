import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


#### Player Setup ####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = player()

#### Title Screen ####
def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()  # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()  # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('           -Play-           ')
    print('           -Help-           ')
    print('           -Quit-           ')
    print(' Copyright 2019 OKJohansen  ')
    print('############################')
    title_screen_selection()


def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('Up, Down, Left, Right = move')
    print('Type the commands to do them')
    print('   Use "look" to inspect    ')
    print('         GL & HF            ')
    print('############################')
    title_screen_selection()


#### MAP ####
"""
a1 a2.. #PLAYER STARTS AT B2
-----------------
|   |   |   |   |  a4
-----------------
| x |   |   |   |  b4 ..
-----------------
|   |   |   |   |
-----------------
|   |   | x | x |
-----------------
"""

ZONENAME = '',
DESCRIPTION = 'description',
EXAMINATION = 'examine',
SOLVED = False,
UP = 'up', 'north',
DOWN = 'down', 'south',
LEFT = 'left', 'west',
RIGHT = 'right', 'east',

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'You can see people selling various goods',
        EXAMINATION: 'It smells like fish',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: 'Settlement',
        DESCRIPTION: 'You see houses, I guess people live here',
        EXAMINATION: 'People live here',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: 'Slums',
        DESCRIPTION: 'This is where the poor people live',
        EXAMINATION: 'You see broken glass and dead cats',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: 'Plains',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: 'Inaccessible',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: 'b1',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!\nYou grew up here,',
        EXAMINATION: 'Your home looks the same - nothing has changed.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: 'Dark Forrest',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: 'Swamps',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: 'Forrest',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'c2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!\nYou grew up here,',
        EXAMINATION: 'Your home looks the same - nothing has changed.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'c3': {
        ZONENAME: 'Dark Forrest',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'c4': {
        ZONENAME: 'Swamps',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },
    'd1': {
        ZONENAME: 'Forrest',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'd2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!\nYou grew up here,',
        EXAMINATION: 'Your home looks the same - nothing has changed.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'd3': {
        ZONENAME: 'Inaccessible',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'd4': {
        ZONENAME: 'Inaccessible',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    }

}


#### GAME INTERACTIVITY ####
def print_location():
    print('\n' + ('#' * (10 + len(myPlayer.location))))
    print('# ' + zonemap[myPlayer.location][ZONENAME] + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (10 + len(myPlayer.location))))


def prompt():
    print("\n" + "========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "look"]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "look"]:
        player_examine(action.lower())
    elif action.lower() in ["examine", "inspect", "look"]:
        player_examine(action.lower())


def player_move(myAction):
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)

def movement_handler(destination):
    print("\nYou have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("There's no puzzle here")
    else:
        print("There is a puzzle here!")


#### GAME FUNCTIONALITY ####

def main_game_loop():
    while myPlayer.game_over == False:
        prompt()
        # here handle if puzzles has been solved, boss defeted, explored etc.


def setup_game():
    os.system('clear')

    #### NAME COLLECTING
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    player_name = input("> ")
    myPlayer.name = player_name

    #### JOB HANDLING
    question2 = "Hello, what role do you want to play?\n"
    question2added = "(You can choose to become a warrior, a mage or a priest?)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    player_job = input("> ")
    valid_job = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_job:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_job:
        print("Choose a valid race")

    #### PLAYER STATS
    if myPlayer.job == "warrior":
        player.hp = 120
        player.mp = 20
    elif myPlayer.job == 'mage':
        player.hp = 40
        player.mp = 120
    elif myPlayer.job == 'priest':
        player.hp = 60
        player.mp = 60

    #### INTRODUCTION
    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure you don't get to lost...\n"
    speech4 = "Hehehehe...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)

    os.system('clear')
    print("####################")
    print("# Let's start now! #")
    print("####################")
    main_game_loop()


title_screen()
