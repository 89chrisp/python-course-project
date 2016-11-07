#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
room seven
"""
import gameItem
import game

descr = """--------------------------------------------------------------------------------
Room no. 7

This is the final room. Other than a terminal on a table there is nothing of
note in this room.
--------------------------------------------------------------------------------
"""
solved = False

roomInv = {}
hint = """
Marvin: 'I bet the terminal is linked to the door just like in the other room.'
"""
look = """
This room has nothing in it but a table, a terminal and the door to the exit.
The door seems even sturdier than the previous ones. The terminal seems
connected to the door."""

door = gameItem.gameItem()
door.name = "door"
door.descr = "A thick, sturdy metallic door. This would be impossible to force"
door.openable = True
door.useable = True
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
    if item == "door":
        if solved:
            print("The door is unlocked.")
        else:
            print("The door is locked.")
    elif item == "terminal":
        terminalFunc2()

def terminalFunc2():
    """
    Function representing a terminal
    """
    global solved
    print("\x1b[2J\x1b[H")
    print("""If you can finish this game you may exit from the door.

There are three rods: a, b and c and 4 disks of different sizes which can slide
onto any rod. The first rod has all 4 disks stacked on top of it arranged in
size with the smallest one on top. Your objective is to move the stack from the
first rod 'a' to the last rod 'c', adhering to the following rules.

    -You may only move one disk at a time
    -A disk can only be moved if it's the uppermost disk
    -You may not stack a disk on top of a smaller one

To move a disk you input the disk number and the rod you wish to move it to,
e.g. '1 c', where 1 is the smallest disk and 4 the largest.
Oh and in order for you to unlock the door you need to complete the game in the
minimum number of moves possible, which is 15 moves for 4 disks.

    1   _|_	   |	     |		     |         |        _|_   1
   2   __|__	   |	     |               |         |       __|__   2
  3   ___|___	   |	     |      --->     |         |      ___|___   3
 4   ____|____	   |	     |		     |         |     ____|____   4
         a         b         c		     a         b         c
You can press 'q' if you want to quit when in the game and 'r' if you want to
retry.""")
    input("Press Enter to continue. ")
    print("\x1b[2J\x1b[H")
    a = [4, 3, 2, 1]
    b = []
    c = []
    source = []
    sources = ""
    moves = 0
    inp = ["1", "2", "3", "4", "a", "b", "c", "q", "r", "cheat"]
    while(True):
        print("")
        print("a {} \nb {} \nc {}" .format(a, b, c))
        print("")
        action = input("Move disk '_' to rod '_': ")
        action_list = action.split(' ')
        if action_list[0] == "q":
            print("Exiting terminal.")
            break
        elif action_list[0] == "cheat":
            print("Way to solve the game with minimum moves:")
            towerR(4, "a", "c", "b")
            continue
        elif action_list[0] == "r":
            print("Retrying...")
            a = [4, 3, 2, 1]
            b = []
            c = []
            moves = 0
            continue
        elif action_list[0] not in inp or action_list[1] not in inp:
            print("\nThat's not valid input. Try again.")
            continue

        disk = int(action_list[0])
        target = action_list[1]

        if disk in a:
            source = a
            sources = "a"
        elif disk in b:
            source = b
            sources = "b"
        elif disk in c:
            source = c
            sources = "c"

        if target == "a":
            t = a
        elif target == "b":
            t = b
        elif target == "c":
            t = c

        if target == sources:
            print("That disk is already on that rod!")

        elif disk != source[-1]:
            print("That disk is not highest on that rod!")

        elif not t:
            print("Moving disk {} from rod {} to rod {}" .format(disk, sources, target))
            source.pop()
            t.append(disk)
            moves += 1
        else:
            if t[-1] < disk:
                print("You can't put a larger disk on a smaller one!")
            else:
                print("Moving disk {} from rod {} to rod {}" .format(disk, sources, target))
                source.pop()
                t.append(disk)
                moves += 1

        if c == [4, 3, 2, 1]:
            print("\nYou made it!\n")
            if moves > 15:
                print("But you used too many moves ({}). " .format(moves))
            else:
                print("You also used the minimum  amount of moves possible({})! " .format(moves))
                print("A familiar 'click' is coming from the door to the exit.")
                solved = True
                game.solved_rooms["seven"] = True
            input("Press Enter to exit the terminal. ")
            break

def towerR(disk, source, target, by):
    """
    Recursive solution to Tower of Hanoi problem
    """
    if disk == 1:
        print("Move disk {} from {} to {}" .format(disk, source, target))
    else:
        towerR(disk-1, source, by, target)
        print("Move disk {} from {} to {}" .format(disk, source, target))
        towerR(disk-1, by, target, source)
