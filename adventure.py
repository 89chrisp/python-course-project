#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game
"""

import argparse
import game

gameMenu = """------------------------------------------
Main Menu

Start               Start the game
Load [filename]     Loads the game from the specified filename
Quit                Quit the game
-------------------------------------------
"""
story = """The game has you starting locked in a room of a house. In order to get out of
the house, which you need to buy food or whatever, you have to navigate through
7 consecutive rooms each with a locked door. You can only get through the door
by solving a small task or puzzles. As always you have your trusty sidekick
Marvin to help you out on your quest. Good luck! (You're gonna need it)"""

#loaded = False
filename = ""

def menu():
    """
    Main method of the game
    """
    print(gameMenu)
    while True:
        action = input()
        actionlist = action.split(" ")
        if action == "s" or action.lower() == 'start':
            print("Starting the game from beginning")
            print("\x1b[2J\x1b[H")
            print(story)
            print("")
            input("Press Enter to start the game")
            game.main()
        elif action == "q" or action.lower() == 'quit':
            action2 = input("Are you sure you want to quit? (y/n): ")
            if action2.lower() == "y":
                return
            elif action2.lower() == "n":
                pass
        elif "load" in action.lower():
            #loaded = True
            if len(actionlist) == 2:
                fname = actionlist[1]
                print("Loading the game from file {}" .format(fname))
                game.loadFunction(fname)
                game.main()
            elif len(actionlist) > 2:
                fname = actionlist[1] + " " + actionlist[2]
                print("Loading the game from file {}" .format(fname))
                game.loadFunction(fname)
                game.main()
            elif len(actionlist) < 2:
                print("You have to provide a filename.")




info = """
The game takes place in a house where your task is to find your way through each
room in order to escape. There are seven rooms, each with its own problem you
need to solve. To your aid you have your trusty pal Mrvin with whom you can
communicate commands and ask for hints. Complete all seven rooms in order to
finish the game.
"""
about = "The author of this game is Christoffer Pihlstrand."
cheat = """The quickest way to solve each room in order is :

one:    move the right painting and use the switch that appears
two:    use the items in the order: bookshelf, torch, bust, deerhead according
        to east, west, south, north as indicated by the author of the book in
        1st room.
three:  use panel, the code is 7373 as written on the note appearing once you
        kick the plant in room 2. You can also use the wire cutter found in the
        table in room one once you have used up 3 attempts on the panel.
four:   Use the terminal. Answer 1: 34, Answer 2, 50, Answer 3: 42
five:   Use the 'look' command to discover the pressure plate. Then use the
        'move' command on the 'crate'. Then use the 'use' command on the
        'left plate'.
six:    pickup the 'sturdy key'. Go back to room 3. Open the 'chest'. Pickup the
        'duck'. Go back to room 6. Use the 'hole'.
seven:  Use the terminal. Type 'cheat' to get the solution to the problem.

You can also use the hidden command 'c [num]' to navigate to rooms (without
solving them). E.g.: c 3 takes you to room 3. Load the file 'cheat' to appear in
the last room with all rooms solved and with all inventory items (not consumed).
"""
parser = argparse.ArgumentParser(description='This program is a game', prog='adventure game')
parser.add_argument("action", nargs='?', default='empty')
parser.add_argument("-i", "--info", action='store_true', help='Displays info about the game')
parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0',
                    help='Displays version of the game and exit')
parser.add_argument("-a", "--about", action='store_true', help='Displays info about the developer')
parser.add_argument("-c", "--cheat", action='store_true', help='Displays how to cheat your way through the game')
args = parser.parse_args()
if args.info:
    print(info)
elif args.about:
    print("")
    print(about)
elif args.cheat:
    print("")
    print(cheat)

if args.action == 'empty':
    input("Press Enter to continue")
    print("\x1b[2J\x1b[H")
    menu()
else:
    print(args.action)
