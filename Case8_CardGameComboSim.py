# -*- coding: utf-8 -*-
"""
Card Combo Simulator
"""

import random as rd
#a deck has 40 cards


decklist = []
hand = []

#function to add cards to decklist
def addCardtoDeck(decklist, name, cost, copies=1):
    cardtoDict = {'Name': name, 'Cost': cost}
    for i in range(0,copies):
        decklist.append(cardtoDict) 
    return decklist
    
#function transfer deck to hand
def addDecktoHand(decklist, hand, times=1):
    for draws in range(0, times):
        card_no_drawn = rd.randint(0,len(decklist)-1)
        card_drawn = decklist.pop(card_no_drawn)
        hand.append(card_drawn)
    return decklist, hand        
                         
#function transfer hand to play


#0. Add Cards to Deck
for i in range(0,40):
    addCardtoDeck(decklist, f'a-{i}', i, copies=1)
    
#1. Add Cards to Hand   
addDecktoHand(decklist,hand,3)

#2. Play Hand to Board

'''
Gameplay
1.) Draw 3 Cards in Deck
2.) Play Cards to Board
    a.) Count followers in play [Rally Count]
    b.)
--End Turn--
'''    