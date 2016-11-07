#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main game
"""
import sys
import json
import one, two, three, four, five, six, seven
import art

current_room = 1        # Variabel för att hålla koll på rum
descr = one.descr       # Variabel för beskrivning av ett rum, one som default
graphic = art.art1      # Variabel för grafisk representation av rum, art1 def
inv = {}                # Inventory för objekt som plockas upp
roomInv = one.roomInv   # Variabel som håller koll på objekt i ett rum
room = one              # Variabel som används för att kommunicera med ett rum
solved = one.solved
solved_rooms = {"one": False, "two": False, "three": False, "four": False,
                "five": False, "six": False, "seven": False}

                        # Håller koll på vilka rum som är lösta
hlp = """
--------------------------------------------------------------------------------
-----------------------------------
i, info             Description of the room
h, help             Displays available commands
f, forward          Continue to the next room if available
b, back             Go back to the previous room
l, look             Look around the room
hi, hint            Provides a clue
x, exit             Exit the program
o, object           Display objects in the room
inv, inventory      Display your inventory
p, pickup [object]  Pickup the object if possible
d, drop [object]    Remove the object from your inventory
ins [object]        Inspect an object for a description
e, use [object]     Use an object
op, open [object]   Open an object
k, kick [object]    Break an object with a powerful kick
m, move [object]    Move an object
save [filename]     Saves the game to file 'filename'
--------------------------------------------------------------------------------
"""

hintc = 0               # Counter då flera hints för ett rum kan förekomma
def main():
    """
    Main loop
    """
    global current_room, hintc
    print("\x1b[2J\x1b[H")      # Clear terminal
    print(descr)                # Print room description
    print(graphic)              # Print graphic
    while True:
        roomFunction(current_room)
        print("Marvin: 'What do you wish to do?'")
        choice = input("->")
        if choice == "i" or choice == "info":
            print("")
            print(descr)
            print("")
        elif choice == "h" or choice == "help":
            print("")
            print(hlp)
            print("")
        elif choice == "f" or choice == "forward":
            print("")
            if solved:
                print("Proceeding to the next room")
                current_room += 1
                roomFunction(current_room)
                input("Press Enter to continue")
                print("\x1b[2J\x1b[H")
                print(descr)
                print(graphic)
            else:
                print("The door to the next room is locked")
            print("")

        elif choice == "b" or choice == "back":
            print("")
            if current_room == 1:
                print("Can't go back, this is the first room")
            else:
                print("Walking back to room no. {}" .format(current_room-1))
                current_room -= 1
                roomFunction(current_room)
                input("Press Enter to continue")
                print("\x1b[2J\x1b[H")
                print(descr)
                print(graphic)
            print("")

        elif choice == "l" or choice == "look":
            if current_room == 5:
                room.look()
            else:
                print(room.look)
            print("")
        elif choice == "hi" or choice == "hint":
            if isinstance(room.hint, str):
                print(room.hint)
            elif isinstance(room.hint, list):
                print(room.hint[hintc])
                hintc += 1
                if hintc >= len(room.hint):
                    hintc = 0

        elif choice == "x" or choice == "exit":
            action = input("Are you sure you want to exit the game? (y/n): ")
            if action == "y":
                sys.exit()
            elif action == "n":
                pass
        elif choice == "o" or choice == "object":
            print("")
            print("The following objects can be seen in the room:")
            for key in roomInv:
                print(key)
            print("")
        #Inventory
        elif choice == "inv" or choice == "inventory":
            print("")
            print("The following items are in your inventory: ")
            if inv:
                for key in inv:
                    print(key)
            else:
                print("Your have nothing in your inventory.")
            print("")
        elif choice.startswith('p') or choice.startswith('pickup'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in roomInv:
                if roomInv[item].storeable:
                    print("{} was added to your inventory" .format(item))
                    a = roomInv.pop(item)
                    inv[item] = a
                    if item == "sturdy key":
                        six.descr = six.descr2
                        six.look = six.look2
                else:
                    print("That item cannot be picked up. ")
            else:
                print("That item is not in the room!")
            print("")

        elif choice.startswith('d') or choice.startswith('drop'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in inv:
                print("{} was removed from your inventory." .format(item))
                a = inv.pop(item)
                roomInv[item] = a
            else:
                print("That item is not in your inventory.")
            print("")

        elif choice.startswith('e') or choice.startswith('use'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in inv:
                if inv[item].useable:
                    print("{} was used" .format(item))
                    useItem(item)
                else:
                    print("That item can't be used.")

            elif item in roomInv:
                if roomInv[item].useable:
                    room.use(item)
                else:
                    print("That item can't be used.")
            else:
                print("That item is not in your inventory.")
            print("")

        elif choice.startswith('ins'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in roomInv:
                print(roomInv[item].descr)
            elif item in inv:
                print(inv[item].descr)
            else:
                print("No such item in the room or your inventory.")
            print("")

        elif choice.startswith('op') or choice.startswith('open'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in roomInv:
                if roomInv[item].openable:
                    room.openItem(item)
                else:
                    print("That item can't be opened.")
            elif item in inv:
                if inv[item].openable:
                    openItem(item)
                else:
                    print("That item can't be opened.")
            else:
                print("No such item in the room.")
            print("")

        elif choice.startswith('k') or choice.startswith('kick'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in roomInv:
                if roomInv[item].kickable:
                    room.kick(item)
                else:
                    print("That item is indestructable!")
            else:
                print("No such item in the room.")
            print("")

        elif choice.startswith('m') or choice.startswith('move'):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                item = choiceList[1]
            elif len(choiceList) > 2:
                item = choiceList[1] + " " + choiceList[2]
            elif len(choiceList) < 2:
                item = ""
            print("")
            if item in roomInv:
                if roomInv[item].moveable:
                    room.move(item)
                else:
                    print("That item can't be moved.")
            else:
                print("No such item in the room.")
            print("")

        elif choice.startswith('c'):
            choiceList = choice.split(' ')
            item = choiceList[1]
            current_room = int(item)
            roomFunction(current_room)
            print(descr)
            print(graphic)

        elif choice.startswith("save"):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                fname = choiceList[1]
                print("Saving the game to file: {}" .format(fname))
                saveFunction(fname)
            elif len(choiceList) > 2:
                fname = choiceList[1] + " " + choiceList[2]
                print("Saving the game to file: {}" .format(fname))
                saveFunction(fname)
            elif len(choiceList) < 2:
                print("You have to provide a filename")

        elif choice.startswith("load"):
            choiceList = choice.split(' ')
            if len(choiceList) == 2:
                fname = choiceList[1]
                print("Loading the game from file: {}" .format(fname))
                loadFunction(fname)
            elif len(choiceList) > 2:
                fname = choiceList[1] + " " + choiceList[2]
                print("Loading the game from file: {}" .format(fname))
                loadFunction(fname)
            elif len(choiceList) < 2:
                print("You have to provide a filename.")

        if current_room == 8:
            print("\nYou did it! You escaped the wicked house! Good Job!")
            sys.exit()


def roomFunction(num):
    """
    Function to handle current room
    """
    global solved, descr, room, roomInv, graphic
    if num == 1:
        solved = one.solved
        roomInv = one.roomInv
        descr = one.descr
        room = one
        graphic = art.art1
    elif num == 2:
        solved = two.solved
        roomInv = two.roomInv
        descr = two.descr
        graphic = art.art2
        room = two
    elif num == 3:
        solved = three.solved
        roomInv = three.roomInv
        descr = three.descr
        graphic = art.art3
        room = three
    elif num == 4:
        solved = four.solved
        roomInv = four.roomInv
        descr = four.descr
        graphic = art.art4
        room = four
    elif num == 5:
        solved = five.solved
        roomInv = five.roomInv
        descr = five.descr
        graphic = art.art5
        room = five
    elif num == 6:
        solved = six.solved
        roomInv = six.roomInv
        descr = six.descr
        graphic = art.art6
        room = six
    elif num == 7:
        solved = seven.solved
        roomInv = seven.roomInv
        descr = seven.descr
        graphic = art.art7
        room = seven
    elif num == 8:
        descr = ""
        graphic = ""


def useItem(item):
    """
    Use item in the inventory
    """
    if item == "note":
        print("The note only reads: 7373")
    elif item == "duck":
        print("You wind up the toy duck and place it on the floor: ")
        print("The duck waddles forwards in a jerky motion.")
        print("Marvin: Hey! Look at it go!")


def openItem(item):
    """
    Open item in the inventory
    """
    if item == "book":
        print("""As you open the book you find the pages are filled with unintelligible text.
The only discernable information is the name of the author: E. W. S. North """)

def saveFunction(fname):
    """
    Saves the game to file using JSON
    """
    roomInvOne = {}
    roomInvTwo = {}
    roomInvThree = {}
    roomInvFour = {}
    roomInvFive = {}
    roomInvSix = {}
    roomInvSeven = {}
    invsOfRooms = [roomInvOne, roomInvTwo, roomInvThree, roomInvFour, roomInvFive,
                   roomInvSix, roomInvSeven]

    #Saving each rooms roomInv dictionairy
    for i in range(1, 8):
        roomFunction(i)
        for k in roomInv:
            invsOfRooms[i-1][k] = roomInv[k].__dict__

    #Saving the current inv dictionairy into invSave
    invSave = {}
    if inv:
        for k in inv:
            invSave[k] = inv[k].__dict__

    # List to wrap all the variables to be saved
    gameSave = [invsOfRooms, invSave, solved_rooms, {"current_room": current_room},
                {"moved": five.moved}, {"code count": three.code_count}]

    #Call to roomFunc to make sure you can keep playing after saving
    roomFunction(current_room)

    #Saving as JSON to file fname
    with open(fname + ".json", 'w') as outfile:
        json.dump(gameSave, outfile, indent=4)

def loadFunction(fname):
    """
    loads the game from file
    """
    global current_room, solved_rooms
    try:
        with open(fname + ".json", 'r') as infile:
            gameSave = json.load(infile)
    except FileNotFoundError:
        print("No such file in directory. ")
        input("Press Enter to continue. ")
        return

    invsOfRooms = gameSave[0]                   # List with the roomInv of all the rooms
    invSave = gameSave[1]                       # Saved inventory
    solved_rooms = gameSave[2]                  # Solved rooms dictionairy
    current_room = gameSave[3]["current_room"]  # Current room variable
    moved = gameSave[4]["moved"]                # Status variable for room 5
    code_count = gameSave[5]["code count"]      # Status variable for room 3

    # Checking status of first room
    if "book" not in invsOfRooms[0]:
        inv["book"] = one.roomInv.pop("book")
    if "switch" in invsOfRooms[0]:
        one.switchItem()
    if "wire cutter" in invsOfRooms[0]:
        one.wire_cutterItem()
    elif "wire cutter" in invSave:
        one.wire_cutterItem()
        inv["wire cutter"] = one.roomInv.pop("wire cutter")

    #Checking status of second room if first was solved
    if solved_rooms["one"]:
        one.solved = True
        if "plant" not in invsOfRooms[1]:
            two.roomInv.pop("plant")
            if "note" in invsOfRooms[1]:
                two.noteItem()
            else:
                two.noteItem()
                inv["note"] = two.roomInv.pop("note")

    #Checking status of third room if second was solved
    if solved_rooms["two"]:
        two.solved = True
        three.code_count = code_count
        if "duck" in invsOfRooms[2]:
            three.duckItem()
        elif "duck" in invSave:
            three.duckItem()
            inv["duck"] = three.roomInv.pop("duck")

    #Checking status of fourth room if third was solved
    if solved_rooms["three"]:
        three.solved = True

    #Checking status of fifth room if fourth was solved
    if solved_rooms["four"]:
        four.solved = True
        if moved:
            five.moved = True
            five.look()

    #Checking status of sixth room if fifth was solved
    if solved_rooms["five"]:
        five.solved = True
        if "sturdy key" not in invsOfRooms[5]:
            inv["sturdy key"] = six.roomInv.pop("sturdy key")

    #Checking status of seventh room if sixth was solved
    if solved_rooms["six"]:
        six.solved = True

    #Checking if seventh rom was solved
    if solved_rooms["seven"]:
        seven.solved = True

    # Call to roomFunc in order play after loading
    roomFunction(current_room)
    print("")
    input("Press Enter to continue")
    print("\x1b[2J\x1b[H")
    print(descr)
    print(graphic)






if __name__ == "__main__":
    main()
