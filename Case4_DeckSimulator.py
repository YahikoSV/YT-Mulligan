# -*- coding: utf-8 -*-
"""
Goals:
    0.) Import a decklist and export deck name
    1.) Odds of Drawing what you want in opening phase
    2.) Add Mulligan Phase Condition
    3.) Simulate Mulligan Phase
    
"""

import urllib.request
import json
import mulliganLib as mLib
import requests
from bs4 import BeautifulSoup as bs

""" March 28, 2024
    0.) Import a decklist and export deck name
   - I did this already for my discord bot now I'm just going to make it specifically for this example    
"""

def decklist(link):
    source = requests.get(link).text
    soup = bs(source, 'lxml')
    
    card_name = soup.find_all('span', class_="el-card-list-info-name-text")
    card_qty = soup.find_all('p', class_="el-card-list-info-count")
    card_cost = soup.select('i[class*="icon-cost is-cost-"]')
    card_stats = soup.find_all('a', class_="el-icon-search is-small tooltipify")
    card_atk = [card['data-card-atk'] for card in card_stats]
    card_def = [card['data-card-life'] for card in card_stats]
    card_type = [card['data-card-char-type'] for card in card_stats]
    
    card_info = []
    for card in range (0,len(card_type)):
        if card_type[card] == '1': #follower
            card_info.append(f'{card_cost[card].text}pp {card_atk[card]}/{card_def[card]}')
        elif card_type[card] == '3': #amulet
            card_info.append(f'{card_cost[card].text}pp Amulet')
        elif card_type[card] == '4': #spell
            card_info.append(f'{card_cost[card].text}pp Spell')
    
    card_list = []
    for unique_card in range(0,len(card_name)):

        for copies in range(0,int(card_qty[unique_card].text[1])):
            card_list.append(f'{card_name[unique_card].text} ({card_info[unique_card]})')
            #card_list.append(f'{card_name[unique_card].text}')
    return card_list



deck_link = 'https://shadowverse-portal.com/deck/1.6.7teBY.7teBY.7teBY.7vtl2.7vtl2.7vtl2.7vuEI.7vuEI.7vuEI.7ePai.7ePai.7ePai.7pr_i.7pr_i.7pvAg.7pvAg.7pvAg.7kWCY.7kWCY.7kWCY.7kYeo.7kYeo.7kYeo.7oMno.7oMno.7oMno.7vydY.7vydY.7vydY.7v_3y.7v_3y.7v_3y.7vwwA.7vwwA.7vwwA.7iDji.7iDji.7iDji.7kYf6.7kYf6?lang=en'
deckList = decklist(deck_link)

"""
1.) Odds of Drawing what in opening phase
- We already coded the odds for something like this earlier
"""

###For example 
#1 Prob. of getting at least 1pp in opening hand
num_total = len(deckList)
num_wanted = 0
for card in deckList:
    if '1pp' in card:
        num_wanted += 1
num_needed = 1
num_draw = 3 


odds = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw)
#You have a 54.5% chance of getting a 1 cost in your starting hand

"""
    2.) Add Mulligan Phase Condition
    Next step let's say I don't draw and do a full mulligan. What's the probability of getting 1 now'  
    Cards discarded from mulligan are temporarily out of the decks thus they are not included in the pool
"""
#2.1 Prob of getting at least 1pp after full mull
num_total = len(deckList) - num_draw
num_draw = 3
num_needed = 1
num_wanted = 0
for card in deckList:
    if '1pp' in card:
        num_wanted += 1
odds_am = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw)

#2.2 Probability of getting at least 1pp after mulligan
prob_mull = 1 - ((1-odds[2])*(1-odds_am[2])) #subtracts odds of not getting it
#Answer is 80.82% let me verify with my brick sheet. 
##Yep, same answer let's go. imagine the excel file I made 6 years ago was still correct (tho I edited it in 2023 because of temporarily discard cards from deck)

"""
But wait there's more because you draw 1-2 cards on your first turn!
"""
#2.3 Probability of getting at least 1pp on turn 1
num_total = len(deckList) - num_draw
num_draw_1st = 1
num_draw_2nd = 2

num_needed = 1
num_wanted = 0
for card in deckList:
    if '1pp' in card:
        num_wanted += 1


odds_1st = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw_1st) #24.32%
odds_2nd = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw_2nd) #43.24%
prob_mull_1st = 1 - ((1-odds[2])*(1-odds_am[2])*(1-odds_1st[2])) #85.48%
prob_mull_2nd = 1 - ((1-odds[2])*(1-odds_am[2])*(1-odds_2nd[2])) #89.11% Correct Way

num_am_1st = 4 #What if we join the cases. (It should not work because the 3 discarded cards will go back to the deck)
num_am_2nd = 5
odds_am_1st = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_am_1st)
odds_am_2nd = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_am_2nd)
prob_am1st = 1 - ((1-odds[2])*(1-odds_am_1st[2])) #85.89%
prob_am2nd = 1 - ((1-odds[2])*(1-odds_am_2nd[2])) #89.74% slight error

"""
Let's create a function
Parameters needed:
    1.) num_deck - num of cards in deck
    2.) num_want - list of num of wanted cards
    3.) num_need - list of num of needed of wanted cards
    4.) num_mull - num of cards to mull if condition is not met
.....
    
    
Before doing that what if i need 2 1pp in hand
If you get 0, discard 3
If you get 1, discard only 2
If you get 2, discard 0

odds_cond_mull = odds_sh2 * odds_amx_xst + odds_sh1 * odds_am2_xst + odds_sh0 * odds_am3_xst
odds_sh2 means odds of getting 2 from starting hand
odds_am2_xst means odds of gentting condition with 2 card mull going xst
"""
#2.4 Prob of getting at least 2pp after mull*
num_total = len(deckList) 
num_draw = 3
num_needed = 2
num_wanted = 0
for card in deckList:
    if '1pp' in card:
        num_wanted += 1
odds_sh_2 = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw)  #12%

num_needed = 1
odds_sh_1 = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw)  #54% 

 

#2.4 Prob of getting at least 2pp after mull*
num_total = len(deckList) 
num_draw = 3
num_needed = 2
num_wanted = 0
for card in deckList:
    if '1pp' in card:
        num_wanted += 1
odds_sh_2 = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw)  #12%

num_needed = 1
odds_sh_1 = mLib.probability_of_at_least_x(num_total, num_wanted, num_needed , num_draw)  #54% 











































