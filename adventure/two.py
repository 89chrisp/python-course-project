#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Room two
"""
import gameItem
import game

descr = """------------------------------------------------------------------------------
Room no. 2

You find yourself in another room without windows. The floor is made of marble.
Each wall has some conspicuous adornment. A head of a horned deer on the wall
to your right. A torch upon the wall straight ahead next to the door leading
forward. To your left is a pedestal with a bust on it. On the same wall as the
door you entered is a bookshelf filled with books.
There is also a plant in one of the corners.
-------------------------------------------------------------------------------
"""
solved = False

roomInv = {}
hint1 = """
The adornements on the walls are surely worth a closer look.
"""
hint2 = """
Have you taken a look around the room?
"""
hint3 = """
Is there a connection to the floor pattern and the adornments?
"""
hint4 = """
Perhaps that book you found earlier could help.
"""
hint = [hint1, hint2, hint3, hint4]
look = """
As you look around the room you see the conspicuous adornements on the walls.
A closer look at the marble floor reveals there is a pattern there.
The pattern depicts the points of a compass with north indicating the wall to
your right as you enter the room."""

switch_combo = [0, 0, 0, 0]

door = gameItem.gameItem()
door.name = "door"
door.descr = "A heavy metallic door. The door seems to be electronically controlled from a panel next to it."
door.openable = True
door.useable = True
roomInv[door.name] = door

switch1 = gameItem.gameItem()
switch1.name = "deerhead"
switch1.descr = "A head of a horned deer decorating the wall. There is something off with the horns..."
switch1.useable = True
roomInv[switch1.name] = switch1

switch2 = gameItem.gameItem()
switch2.name = "torch"
switch2.descr = "An unlit torch on the wall."
switch2.useable = True
roomInv[switch2.name] = switch2

switch3 = gameItem.gameItem()
switch3.name = "bust"
switch3.descr = "The plaque of the bust only reads: Famous author of 'Secrets to move forward'."
switch3.useable = True
roomInv[switch3.name] = switch3

switch4 = gameItem.gameItem()
switch4.name = "bookshelf"
switch4.descr = "A bookshelf filled with books. One looks more worn than the rest..."
switch4.useable = True
roomInv[switch4.name] = switch4

plant = gameItem.gameItem()
plant.name = "plant"
plant.descr = "A rather largre plant in a clay pot."
plant.kickable = True
roomInv[plant.name] = plant

def noteItem():
    """
    Creates a note
    """
    note = gameItem.gameItem()
    note.name = "note"
    note.descr = "There is something scribbled on the note"
    note.useable = True
    note.storeable = True
    roomInv[note.name] = note

def openItem(item):
    """
    Opens item
    """
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

    elif item == "book":
        print("""As you open the book you find the pages are filled with unintelligible text.
The only discernable information is the name of the author: E. W. S. North """)

def kick(item):
    """
    Kicks item
    """
    if item == "plant":
        print("The pot beaks as you kick it. You see a note among the dirt and rubble.")
        del roomInv["plant"]
        noteItem()




#def move(item):
#    """
#    Moves item
#    """
#    pass

def use(item):
    """
    Use the item
    """
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")

    elif item == "deerhead":
        print("You pull one of horns of the deerhead and hear a click sound.")
        switch_combo.pop(0)
        switch_combo.append(1)
        switch()
    elif item == "torch":
        print("The torch moves as a lever when you pull it: 'click'")
        switch_combo.pop(0)
        switch_combo.append(2)
        switch()
    elif item == "bust":
        print("One of the ears of the bust looks a bit strange, you turn it: 'click'")
        switch_combo.pop(0)
        switch_combo.append(3)
        switch()
    elif item == "bookshelf":
        print("You pull out the worn book from the bookshelf: 'click'")
        switch_combo.pop(0)
        switch_combo.append(4)
        switch()

    elif item == "note":
        print("The note only reads: 7373")

def switch():
    """
    Checks to see if the switchorder is corrects and then unlocks the door
    """
    global solved
    if switch_combo == [4, 2, 3, 1]:
        print("\nAnother 'click' coming from the door")
        solved = True
        game.solved_rooms["two"] = True
    else:
        solved = False
