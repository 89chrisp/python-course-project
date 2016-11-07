#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Room three
"""
import gameItem
import game
# import one
"""
Room three
"""
descr = """--------------------------------------------------------------------------------
Room no. 3

You find yourself in another room without windows.
There is a rather large chest in the room and a small panel next to the metallic
door which leads to the next room.
--------------------------------------------------------------------------------
"""
solved = False

roomInv = {}
hint1 = """Marvin: 'That panel is surely the key to moving forward.'
"""
hint2 = "Marvin: 'I usually hide my key or code in something.'"
hint3 = "Marvin: 'Wasn't there a plant in the previous room? Good hiding place.'"
hint = [hint1, hint2, hint3]
hint4 = "Marvin: 'That panel looks like it's quite easy to open. "

look = """The room is rather lackluster in terms of furnishings. There is a prominent
looking chest on the floor next to one of the walls...
There is also a small panel next to the heavy metallic door."""

door = gameItem.gameItem()
door.name = "door"
door.descr = "A heavy metallic door. The door seems to be electronically controlled from a panel next to it."
door.openable = True
door.useable = True
roomInv[door.name] = door

panel = gameItem.gameItem()
panel.name = "panel"
panel.descr = "The panel has a numpad on it. This kind of panel usually only allows three failed attempts..."
panel.openable = True
panel.useable = True
roomInv[panel.name] = panel

chest = gameItem.gameItem()
chest.name = "chest"
chest.descr = "A sturdy chest with a heavy lock. This thing won't break, you'll have to find a key."
chest.openable = True
roomInv[chest.name] = chest

broken = False
code_count = 0

def openItem(item):
    """
    Opens item
    """
    global solved
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

    elif item == "panel":
        if code_count < 3:
            print("Marvin: Maybe you should try the code first?")
        elif "wire cutter" in game.inv:
            print("You open the panel and see a bunch of wires.")
            print("Marvin: 'It's probably the red one'")
            print("You bypass the lock mechanism using the wire cutter: 'click'")
            solved = True
            game.solved_rooms["three"] = True
        else:
            print("""You open the panel and see a bunch of wires. Now what? If only
you had something to cut the wires with...""")

    elif item == "chest":
        if "sturdy key" in game.inv:
            if "duck" not in game.inv:
                print("The chest opens.")
                print("...")
                print("There is a small wind-up duck toy in the chest...")
                duckItem()
            else:
                print("The chest is empty.")

        else:
            print("You need a key to do that.")

# def kick(item):
#     """
#     Kicks item
#     """
#     pass


# def move(item):
#     """
#     Moves item
#     """
#     pass

def use(item):
    """
    Use the item
    """
    global solved, code_count, broken
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

    elif item == "panel":
        if code_count < 3:
            code = input("Put in the numbers on the numpad: ")
            try:
                val = int(code)
                if val == 7373:
                    print("You hear a click from the lock mechanism of the door.")
                    solved = True
                    game.solved_rooms["three"] = True
                else:
                    print("That doesn't seem to be the right code.")
                    code_count += 1
            except ValueError:
                print("You have to put in numbers not letters!")

        else:
            print("You made too many attempts. The panel has locked down!")
            print("Perhaps you can bypass the panel somehow...")
            if not broken:
                hint.append(hint4)
                game.hintc = 3
                broken = True

    elif item == "duck":
        print("You wind up the toy duck and place it on the floor: ")
        print("The duck waddles forwards in a jerky motion.")
        print("Marvin: Hey! Look at it go!")

def duckItem():
    """
    Creates a duck item.
    """
    duck = gameItem.gameItem()
    duck.name = "duck"
    duck.descr = "A small wind-up toy in the shape of a duck."
    duck.useable = True
    duck.storeable = True
    roomInv[duck.name] = duck
