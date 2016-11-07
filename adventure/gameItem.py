#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gameItem class for objects in game
"""
class gameItem:
    """
    gameItem is a class used to describe items in the game.
    available attributes are:

    name                string with name of item
    descr               string describing the item
    openable            boolean
    kickable            boolean
    moveable            boolean
    useable             boolean
    storeable           boolean
    """
    def __init__(self):
        self.name = ""
        self.descr = ""
        self.openable = False
        self.kickable = False
        self.moveable = False
        self.useable = False
        self.storeable = False
