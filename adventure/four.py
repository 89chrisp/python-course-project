#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
room four
"""
import gameItem
import game

descr = """--------------------------------------------------------------------------------
Room no. 4

In this dull room there is a terminal on top of a wooden table. Other than that
the room is completely void of both decorations and windows. The only other item
is the solid looking door leading to the next room.
--------------------------------------------------------------------------------
"""
solved = False

roomInv = {}
hint = """Marvin: 'That terminal sure looks conspicuous, it must have something to
to with the door. Why not use it?'
"""
look = """
There is not much to look at in this room. The terminal on the table seems to be
connected to the door leading to the next room.
"""

door = gameItem.gameItem()
door.name = "door"
door.descr = "A solid door. The door lock is connected to the terminal."
door.useable = True
door.openable = True
roomInv[door.name] = door

table = gameItem.gameItem()
table.name = "table"
table.descr = "A wooden rectangular table with a terminal on it."
roomInv[table.name] = table

terminal = gameItem.gameItem()
terminal.name = "terminal"
terminal.descr = "A terminal. Perhaps you should use it for more information."
terminal.useable = True
roomInv[terminal.name] = terminal


def openItem(item):
    """
    Opens item
    """
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

# def kick(item):
#     """
#     Kicks item
#     """


# def move(item):
#     """
#     Moves item
#     """
#     pass

def use(item):
    """
    Use the item
    """
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

    elif item == "terminal":
        terminalFunc()

def terminalFunc():
    """
    Function for the terminal
    """
    global solved
    solved_problems = 0
    print("\x1b[2J\x1b[H")
    print("Answer these question correctly and you may proceed to the next room: \n")
    print("""In a meeting of the governing representatives of a secret council,
all the leaders are seated around a large circular table. A heated discussion
arises between council man number six and number nineteen. The council men are
four seats short of being seated opposite to each other.
How many council men are there? """)
    while True:
        answer = input("Answer: ")
        try:
            answer = int(answer)
            if answer == 34:
                input("Press Enter to continue.")
                solved_problems += 1
                break
            else:
                input("Press Enter to continue.")
                break
        except ValueError:
            print("You have to put in numbers not letters!")
            continue
    print("\x1b[2J\x1b[H")
    print("""Problem 2.
Imagine there is a very large cucumber weighing 100 kg. The cucumber is
comprised of 99% water. The cucumber is left out in the sun to dry. When it's
taken inside again it consists of 98% water.
How much does the cucumber weigh now? """)
    while True:
        answer = input("Answer in kg: ")
        try:
            answer = int(answer)
            if answer == 50:
                input("Press Enter to continue.")
                solved_problems += 1
                break
            else:
                input("Press Enter to continue.")
                break
        except ValueError:
            print("You have to put in numbers not letters!")
            continue
    print("\x1b[2J\x1b[H")
    print("""Problem 3.
Bosse has three children. Robert, Kurt and Fred. Robert is twice as old as Kurt.
Fred is three years younger than Robert. Fred was six when they got their cat
Cleo as a kitten three years ago. Bosse is 7 times older than Kurt.
How old is Bosse?""")

    while True:
        answer = input("Answer in years: ")
        try:
            answer = int(answer)
            if answer == 42:
                input("Press Enter to continue.")
                solved_problems += 1
                break
            else:
                input("Press Enter to continue.")
                break
        except ValueError:
            print("You have to put in numbers not letters!")
            continue

    if solved_problems > 2:
        print("------------------------")
        print("You answered all problems correct!")
        print("You hear the door 'click' as it unlocks.")
        solved = True
        game.solved_rooms["four"] = True
    else:
        print("You answered one or more problems incorrectly.")
