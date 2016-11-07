#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
room five
"""
import gameItem
import game

descr = """--------------------------------------------------------------------------------
Room no. 5

This room has a weird pattern on the floor. Other than that it seems empty save
for a crate lying about.
--------------------------------------------------------------------------------
"""
solved = False
moved = False
roomInv = {}
hint1 = """Marvin: 'Hmm this room looks quite empty. You should take a look around though.'
"""
hint = [hint1]


looktext = """
Looking around the suspiciously empty room you can't see anything of note except
for the crate. A closer look around the awful floor almost makes you dizzy due
to the ugly pattern. Suddenly you hear a 'click'. You stepped on something!"""

door = gameItem.gameItem()
door.name = "door"
door.descr = "Another sturdy unbreakable door..."
door.useable = True
door.openable = True
roomInv[door.name] = door

crate = gameItem.gameItem()
crate.name = "crate"
crate.descr = "A large crate. It's rather heavy but you can probably shove it. "
crate.moveable = True
roomInv[crate.name] = crate

look_count = 0

def look():
    """
    Function triggered by look command
    """
    global look_count
    if not moved:
        print(looktext)
    if look_count == 0:

        ppl = gameItem.gameItem()
        ppl.name = "left plate"
        ppl.descr = "A pressure plate which activates as you step on it."
        ppl.useable = True
        roomInv[ppl.name] = ppl

        ppr = gameItem.gameItem()
        ppr.name = "right plate"
        ppr.descr = "A pressure plate which activates as you step on it."
        ppr.useable = True
        roomInv[ppr.name] = ppr

        look_count += 1
        hint2 = """Marvin: 'Perhaps both pressure plates need to be triggered.'
        """
        hint.append(hint2)
    else:
        pass

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
#     pass

def move(item):
    """
    Moves item
    """
    global moved
    if item == "crate":
        if look_count > 0:
            if moved:
                print("You move the crate away from the pressure plate.")
                print("'Click'")
                moved = False
            else:
                print("You move the crate with some difficulty to the right pressure plate. ")
                print("'Click'")
                moved = True
        else:
            print("You move the crate with some difficulty. ")
            print("...")

def use(item):
    """
    Use the item
    """
    global solved
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")
    elif item == "left plate" and moved:
        print("The pressure plate sinks down with a 'click' as you step on it.")
        print("You hear a second click coming from the door.")
        print("The pressure plate remains sunken down as you step off.")
        solved = True
        game.solved_rooms["five"] = True
    elif item == "right plate" and moved:
        print("You can't use that right now. There is a crate on it.")
    elif item == "left plate" or item == "right plate":
        print("The pressure plate sinks down with a 'click' as you step on it.")
        print("Nothig happens.")
        print("The pressure plate raises with a click as you step off.")
