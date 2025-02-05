# -*- coding: utf-8 -*-
"""
Card Combo Simulator
"""

import random as rd
#a deck has 40 cards




#function to add cards to decklist
def addCardtoDeck(decklist, name, cost, copies=1):
    cardtoDict = {'Name': name, 'Cost': cost}
    for i in range(0,copies):
        decklist.append(cardtoDict) 
    return decklist
    
#function transfer deck to hand
def addDecktoHand(decklist, hand, times=1):
    for draws in range(0, times):
        decklist, card_drawn = choseAndRemoveCard(decklist)
        hand.append(card_drawn)
    return decklist, hand        
                         
#function transfer hand to play
def playCard(hand, board, **condition):
    for kind, desc in condition.items():
        if kind == 'Cost':
            split_desc = mySplit(desc)
            print(split_desc)
            costlist = [hand[i]['Cost'] for i in range(0,len(hand))]
            print(costlist)
            qualified_indices = findIndicesFromInequality(split_desc[0], int(split_desc[1]), costlist)
            
            if qualified_indices != []:
                card_no_drawn = rd.choice(qualified_indices)
                card_drawn = hand.pop(card_no_drawn)  
                board.append(card_drawn)
            else:
                card_drawn = {}
    return hand, board, card_drawn


### Back-end functions ###

# Split String to get number left
def mySplit(s):  #https://stackoverflow.com/questions/430079/how-to-split-strings-into-text-and-number
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    return head, tail

# String to Inequality
def findIndicesFromInequality(inequality, value, desclist):
    if inequality == '<':
        return [i for i in range(len(desclist)) if desclist[i] < value]      
    elif inequality == '<=':
        return [i for i in range(len(desclist)) if desclist[i] <= value]      
    elif inequality == '=':
        return [i for i in range(len(desclist)) if desclist[i] == value]    
    elif inequality == '>=':
        return [i for i in range(len(desclist)) if desclist[i] >= value]      
    elif inequality == '>':
        return [i for i in range(len(desclist)) if desclist[i] > value]  
    elif inequality == '!=':
        return [i for i in range(len(desclist)) if desclist[i] != value]     
    else:
        return []
    
# Chose and Remove Chosen Card
def choseAndRemoveCard(cardlist):
        card_no_drawn = rd.randint(0,len(cardlist)-1)
        card_drawn = cardlist.pop(card_no_drawn)    
        return cardlist, card_drawn
    
    
# #A.) get index by a property         
# def getIndexByProperty(deck,card_property,card_desc):
#     for i, dic in enumerate(deck):
#         if dic[card_property] == card_desc:
#             return i
#     return None    


decklist = []
hand = []
board = []
pp_max = 0

#2c. Play Hand to Board



'''
Gameplay
1.) Draw 3 Cards in Deck
2.) Play Cards to Board
    a.) Count followers in play [Rally Count]
    b.) Set pp limit per turn 1-10 max
--End Turn--
'''    

#0. Add Cards to Deck
for i in range(0,40):
    addCardtoDeck(decklist, f'a-{i}', (i+9)//9, copies=1)
    
#1. Add Cards to Hand   
decklist, hand = addDecktoHand(decklist,hand,3)
print(hand)


#2. A Turn Starts
for i in range(0,10):
    
    #2a. Set Max PP
    pp_max = pp_max + 1
    print(f'Turn {pp_max}')
    #2b. Draw a card
    
    decklist, hand = addDecktoHand(decklist,hand,1)
    #2c. Play valid as many valid cards to board as possible
    pp_left = pp_max
    card_drawn = {'card':'True'} #dummy
    while pp_left > 0 and card_drawn != {}:
        hand, board, card_drawn = playCard(hand, board, Cost=f'<={pp_left}')  
        if card_drawn != {}:
            pp_left = pp_left - card_drawn['Cost']
    print('Hand:',hand)
    print('Board:',board)
    print('Rally:', len(board))
    #End Turn
    


