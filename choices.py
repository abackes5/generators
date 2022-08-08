# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:34:27 2022

@author: abackes
"""


def start():
    print("Welcome, adventurer. Please choose a class: \nMage    Fighter    Rogue")
    clas=input("> ")    
    stats(clas)
    print("You have chosen {}. An excellent choice. \nBut what is your name?" .format(clas))
    name = input("> ")
    print("{}, through luck or misfortune, you have arrived at the entrance to a cavern." .format(name))
    print("Will you enter with courage?")
    print("Y/N")
    enter_v = input("> ")
    if enter_v == ("N" or "n"):
        print("Well, that is unfortunate indeed.")
    else:
        print("Indeed, you have no reason for fear.\n\n")
        enter()
        
def stats(clas):
    if clas == "mage" or clas == "Mage":
        hp = 42
    elif clas == "fighter" or clas == "Fighter":
        hp = 63
    elif clas == "rogue" or clas == "Rogue":
        hp = 48
    else:
        print("That is not a valid input.")
        start()
    print("Your HP is", hp)
        
def enter():
    print("The cavern is wet, as caverns are wont to be.\nIt's quiet in here.")
    print("Is it... too quiet?")
    print("Y/N")
    #quiet = input("> ")
    print("Well, as I said, there's nothing to fear.")
    print("*A loud noise echoes through the chamber*")


def combat():
    print("You have now entered combat.")
    while hp > 0:
        print("It is your turn.")
        hp = hp - 1
    
    
    
    
hp = 40

stats("mage")


