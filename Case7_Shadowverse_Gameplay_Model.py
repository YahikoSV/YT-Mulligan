
import copy
import random as rd
import xlwings as xw # pip install xlwings
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import Shared_Databases as sd
import numpy as np

deck = {"brand":{"Ford":"tabe"} }
wb = xw.Book('Decklists.xlsx')
wb.sh


# cardA = {
#           "Name"  : "Calby"
#          ,"Class" : "Shadow"
#          ,"Trait" : "Chess"
#          ,"Type"  : "Follower"
#          ,'Cost'  : 2
#          ,'Atk_Unevo'   : 2
#          ,'HP_Unevo'    : 2
#          ,'Atk_Evo'     : 4
#          ,'HP_Evo'      : 4
#          ,'Skill_Unevo' : "Fanfare: I cheese your face"
#          ,'Skill_Evo'   : "Evolve: I declare Minthe is my wife"
#         }


# # deck = [cardA,cardA]
# # deck = [deck.append(copy.deepcopy(cardA)) for i in range(0,40)]


# # 40 Card Deck
# deck = [(copy.deepcopy(cardA)) for i in range(0,40)]
# for i in range(0,len(deck)):
#     deck[i]['Name'] = str(i) 
# # hand

hand = []
board = []
mull_void = []
deck = copy.deepcopy(deckList)

#We need name,class,trait,cost,atk_unevo,atk_evo,hp_unevo,hp_evo,skill_unevo,skill_evo,skill_nf
deckLink = 'https://shadowverse-portal.com/deck/3.5.7tiao.7tiao.7tiao.7teBY.7teBY.7teBY.7gFVQ.7gFVQ.7gFVQ.7k8Ww.7k8Ww.7k8Ww.7nwDg.7rmow.7rmow.7rmow.7pvAg.7pvAg.7pvAg.7kAEc.7kAEc.7kAEc.7n-Nc.7n-Nc.7n-Nc.7vcfS.7vcfS.7vcfS.7iDji.7iDji.7iDji.7tb-w.7tb-w.7tb-w.7vcfc.7vcfc.7vcfc.7vcfI.7vcfI.7vcfI?lang=en'
deckList = decklist(deckLink)
deck = copy.deepcopy(deckList)
#0.) Create a deck
def decklist(link):
    source = requests.get(link).text
    soup = bs(source, 'lxml')
    
    card_name = soup.find_all('span', class_="el-card-list-info-name-text")
    card_qty = soup.find_all('p', class_="el-card-list-info-count")
    card_cost = soup.select('i[class*="icon-cost is-cost-"]')
    card_stats = soup.find_all('a', class_="el-icon-search is-small tooltipify")
    
    card_trait     = [card['data-card-tribe-name'] for card in card_stats]
    card_atk_unevo = [card['data-card-atk'] for card in card_stats]
    card_hp_unevo  = [card['data-card-life'] for card in card_stats]
    card_atk_evo   = [card['data-card-evo-atk'] for card in card_stats]
    card_hp_evo    = [card['data-card-evo-life'] for card in card_stats]     
    card_type      = [card['data-card-char-type'] for card in card_stats]
    card_skill_unevo = [card['data-card-skill-disc'] for card in card_stats]
    card_skill_evo   = [card['data-card-evo-skill-disc'] for card in card_stats]
    card_href        = [card['href'] for card in card_stats]
    
    card_class     = [sd.identifyClass(int(href[9])) for href in card_href]
    card_type_rev  = [sd.identifyCardType(int(card_type_no)) for card_type_no in card_type]
        
    deckList = []
    for unique_card in range(0,len(card_name)):
        for copies in range(0,int(card_qty[unique_card].text[1])):
            deckList.append(
                {
                  "Name"  : card_name[unique_card].text
                 ,"Class" : card_class[unique_card]
                 ,"Trait" : card_trait[unique_card]
                 ,"Type"  : card_type_rev[unique_card]
                 ,'Cost'  : int(card_cost[unique_card].text)
                 ,'Atk_Unevo'   : int(card_atk_unevo[unique_card])
                 ,'HP_Unevo'    : int(card_hp_unevo[unique_card])
                 ,'Atk_Evo'     : int(card_atk_evo[unique_card])
                 ,'HP_Evo'      : int(card_hp_evo[unique_card])
                 ,'Skill_Unevo' : card_skill_unevo[unique_card]
                 ,'Skill_Evo'   : card_skill_evo[unique_card]                   
                    }
                )
    return deckList

#1.) draw function
def draw(deck, hand, total_draws):
    for draws in range(0,total_draws):
        card_no_drawn = rd.randint(0,len(deck)-1)
        card_drawn = deck.pop(card_no_drawn)
        hand.append(card_drawn)
    
    return deck, hand

###deck, hand = draw(deck, hand, 40)


#2.) play function
def playFromHand(hand, board, card_name_played):
    card_no_played = getIndexByProperty(hand,'Name',card_name_played)
    card_played = hand.pop(card_no_played)
    board.append(card_played)    
    return hand, board
 
#3. ) discard function
def discardFromHand(hand, card_name_discarded):
    card_no_discarded = getIndexByProperty(hand,'Name',card_name_discarded)
    card_discarded = hand.pop(card_no_discarded) 
    return hand 





#A.) get index by a property         
def getIndexByProperty(deck,card_property,card_desc):
    for i, dic in enumerate(deck):
        if dic[card_property] == card_desc:
            return i
    return None    

#B.) get list in a property
def getListByProperty(deck,card_property,card_desc):
    list_qualified_cards = []
    for i, dic in enumerate(deck):
        if dic[card_property] == card_desc:
            list_qualified_cards.append(dic)
    return list_qualified_cards 


# wb = xw.Book('Decklists.xlsx')
# wb.sheets['Test']['B1'].value



