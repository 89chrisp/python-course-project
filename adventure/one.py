#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Room one
"""
import gameItem
import game

descr = """-------------------------------------------------------------------------------
Room no. 1

You find yourself in a room without windows.

There is a table in the room and the walls are decorated with some paintings.
There is also a book upon the table.
-------------------------------------------------------------------------------
"""
solved = False
roomInv = {}
hint = """
There are some strange marks on the wall next to one of the paintings...
"""
look = """
As you look around the room you see a worn table and some mundane paintings
decorating the walls. There is a book lying on the table.

A sturdy door is the only exit from the room.
"""

door = gameItem.gameItem()
door.name = "door"
door.descr = "A sturdy door which looks too solid to force..."
door.openable = True
door.useable = True
roomInv[door.name] = door


table = gameItem.gameItem()
table.name = "table"
table.descr = "A wooden rectangular table with a drawer attached."
table.openable = True
roomInv[table.name] = table

painting_1 = gameItem.gameItem()
painting_1.name = "left painting"
painting_1.descr = "A painting depicting a boat."
painting_1.moveable = True
roomInv[painting_1.name] = painting_1

painting_3 = gameItem.gameItem()
painting_3.name = "right painting"
painting_3.descr = "A painting depicting a cow. This painting looks more worn."
painting_3.moveable = True
roomInv[painting_3.name] = painting_3

painting_2 = gameItem.gameItem()
painting_2.name = "middle painting"
painting_2.descr = "A painting depicting a meadow."
painting_2.moveable = True
roomInv[painting_2.name] = painting_2

book = gameItem.gameItem()
book.name = "book"
book.descr = "The title reads 'Secrets to move forward'."
book.openable = True
book.storeable = True
roomInv[book.name] = book


def wire_cutterItem():
    """
    Creates the wire_cutter
    """
    wire_cutter = gameItem.gameItem()
    wire_cutter.name = "wire cutter"
    wire_cutter.descr = "Used for cutting wires."
    wire_cutter.storeable = True
    roomInv[wire_cutter.name] = wire_cutter


def switchItem():
    """
    Creates a switch item in the room
    """
    switch = gameItem.gameItem()
    switch.name = "switch"
    switch.descr = "A small switch hidden behind the painting"
    switch.useable = True
    roomInv[switch.name] = switch

def openItem(item):
    """
    Opens item
    """
    if item == "book":
        print("""As you open the book you find the pages are filled with unintelligible text.
The only discernable information is the name of the author: E. W. S. North """)

    elif item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

    elif item == "table":
        if "wire cutter" not in game.inv:
            print("You open the drawer of the table. There is a wire cutter inside.")
            wire_cutterItem()
        else:
            print("The drawer is empty. ")


# def kick(item):
#     """
#     Kicks item
#     """

def move(item):
    """
    Moves item
    """
    if item == "left painting":
        print("""The painting slides to the side as you move it and then returns
roughly to its original position.""")

    elif item == "middle painting":
        print("""The painting slides to the side as you move it and then returns
roughly to its original position.""")

    elif item == "right painting":
        print("""The painting slides to the side as you move it. There is a small
switch behind the painting!""")
        switchItem()

def use(item):
    """
    Uses the item
    """
    global solved
    if item == "switch":
        print("""As you press the switch there is a subtle 'click' sound coming
from the locked door...""")
        solved = True
        game.solved_rooms["one"] = True

    elif item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")
