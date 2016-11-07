#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
room six
"""
import gameItem
import game

descr = """--------------------------------------------------------------------------------
Room no. 6

Another empty room. Wait, there is a key hanging on the wall!
There is also a hole in one of the walls.
--------------------------------------------------------------------------------
"""
solved = False

roomInv = {}
h1 = """Marvin: 'Maybe the key doesn't work on this door, but something else we encountered earlier.'
"""

h2 = """Marvin: 'There must be something to that hole.'
"""

hint = [h1, h2]

look = """
As you look around the room you see a key hanging on the wall. You also see a
hole in one of the walls. As there is nothing else of note, the hole must surely
be important.
"""
descr2 = """--------------------------------------------------------------------------------
Room no. 6

Another empty room. There is a hole in one of the walls.
--------------------------------------------------------------------------------
"""
look2 = """
As you look around the room you see a hole in one of the walls. As there is
nothing else of note, the hole must surely be important.
"""


door = gameItem.gameItem()
door.name = "door"
door.descr = "A sturdy door which looks too solid to force..."
door.useable = True
door.openable = True
roomInv[door.name] = door

sturdy_key = gameItem.gameItem()
sturdy_key.name = "sturdy key"
sturdy_key.descr = "A sturdy key. I'm sure it fits some lock in these rooms."
sturdy_key.storeable = True
roomInv[sturdy_key.name] = sturdy_key

hole = gameItem.gameItem()
hole.name = "hole"
hole.descr = "A look insde the hole reveals there's a button inside. But the hole is quite small. "
hole.useable = True
roomInv[hole.name] = hole

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


# def move(item):
#     """
#     Moves item
#     """
#     pass

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
    elif item == "hole":
        if "duck" in game.inv:
            print("You wind up the duck and place it inside the hole.")
            print("The duck waddles forward until it reaches the button at the end of the hole")
            print("'Click'")
            solved = True
            game.solved_rooms["six"] = True
            game.inv.pop("duck")
        else:
            print("The hole is just small enough so your hands can't fit through the opening. ")
            if len(hint) == 2:
                hint.append("""
Perhaps a small item can fit through the hole.
""")
                game.hintc = 2
            else:
                pass
