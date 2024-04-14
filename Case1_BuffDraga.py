# -*- coding: utf-8 -*-
"""
Question: What is the mulligan to increase the odds of 4 buffs on turn 3.
A. Keep 1 cost 1 buff
B. Keep 2 cost 1 buff
C. Keep 1 cost 2 buff
D. Keep 2 cost 2 buff

Before starting the analysis we have to remember how to upload decks from deckcode.
1.) Deckcode to deck [done 240303]
2.) Count how many 1 cost and 2 cost that are in the deck
3.) Count how many 1 cost and 2 cost buff are in the deck


Then for the analysis part
4.) No Mulligan case
5.) Add mulligan segment draw 3, no repetition (how to get all cases in mulligan)
6.) Moments where order
"""



#1.) Imported from SV Bit

import urllib.request
import json
import mulliganLib as mLib

def createlinkfromcode(deck_code, lang, mode, valid_input = False):
    sv_format = {'R':'3', 'U':'1','T':'2'}
    languages = ['en', 'ja', 'ko', 'zh-tw' , 'fr', 'it', 'de', 'es']
    
    deck_code_url = "https://shadowverse-portal.com/api/v1/deck/import?format=json&deck_code=" + deck_code + "&lang=en"
    with urllib.request.urlopen(deck_code_url) as response:
            source = response.read()            
    deck_json = json.loads(source)
    
    if len(deck_json['data']['errors']) != 0:
        response = "Deck code invalid or does not exist"
    elif mode.upper() not in sv_format:
        response = "Invalid deck format"
    elif lang.lower() not in languages:
        response = "Invalid language"
    else:      
        deck_hash = deck_json['data']['hash']
        #deck_hash = deck_hash.replace("1",str(sv_format[mode.upper()]),1)
        
        deck_list_url = "https://shadowverse-portal.com/deck/" + str(deck_hash) + "?lang=" + str(lang)
        response = deck_list_url
        valid_input = True
    return response, valid_input 

deckLink = 'https://shadowverse-portal.com/deck/1.4.7fsM2.7fsM2.7fsM2.7nUeM.7nUeM.7nUeM.7ft4w.7ft4w.7fuoI.7fuoI.7fuoI.7fxEi.7fxEi.7fxEi.7rInM.7rInM.7rInM.7nVMw.7nVMw.7nVMw.gXTM4.gXTM4.gXTM4.7iDji.7iDji.7iDji.7fxEY.7fxEY.7fxEY.7jixS.7jixS.7fzgy.7fzgy.7fzgy.7rNfi.7rNfi.7rNfi.7c9Xy.7c9Xy.7c9Xy?lang=en'


import requests
from bs4 import BeautifulSoup as bs

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
    return card_list

deckList = decklist(deckLink)


'''
Main problem it only features the decklist screen therefore there are no card info text.
Wait there is!
'''

#Odds of getting 4 buff at turn 3
num_draw_1st = 6
num_draw_2nd = 7
num_total = 40
num_1_cost_buff      = 8
num_1_cost_buff_need = 2
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12
num_2_cost_buff_need = 2
num_2_cost_buff_max  = 2
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

###Case 1: draw naturally with 6-7 cards (1st)
P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-15.09%, 2nd-25.02%

###Case 2: I got 2 1cost buff pre-draw
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 - 2
num_1_cost_buff_need = 2 - 2
num_1_cost_buff_max  = num_1_cost_buff 
num_2_cost_buff      = 12
num_2_cost_buff_need = 2
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-20.93%, 2nd-34.58%



###Case 2: I got 2 2cost buff pre-draw
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 
num_1_cost_buff_need = 2 
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12 - 2
num_2_cost_buff_need = 2 - 2
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-9.64%, 2nd-17.23%



###Case 3: I got 1 2cost and 1 1cost buff pre-draw
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 - 1
num_1_cost_buff_need = 2 - 1
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12 - 1
num_2_cost_buff_need = 2 - 1
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-23.38%, 2nd-37.24%


###Case 3B: I got 1 2cost and 1 1cost buff pre-draw (add 1 1pp buff)
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 - 1 + 1
num_1_cost_buff_need = 2 - 1
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12 - 1
num_2_cost_buff_need = 2 - 1
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-26.27%, 2nd-41.21%

###Case 3C: I got 1 2cost and 1 1cost buff pre-draw (add 3 1pp buff)
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 - 1 + 3
num_1_cost_buff_need = 2 - 1
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12 - 1
num_2_cost_buff_need = 2 - 1
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-31.73%, 2nd-48.26%

'''
Conclusion: always aim for a 1 2cost/1cost
'''

###Case 4: I got 2 1cost and 1 2cost buff pre-draw
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 - 2
num_1_cost_buff_need = 2 - 2
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12 - 1
num_2_cost_buff_need = 2 - 1
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-63.02%, 2nd-74.01%

###Case 5: I got 1 1cost and 2 2cost buff pre-draw
num_draw_1st = 3
num_draw_2nd = 4
num_total = 40
num_1_cost_buff      = 8 - 1
num_1_cost_buff_need = 2 - 1
num_1_cost_buff_max  = num_1_cost_buff
num_2_cost_buff      = 12 - 2
num_2_cost_buff_need = 2 - 2
num_2_cost_buff_max  = num_2_cost_buff
num_wanted = [num_1_cost_buff, num_2_cost_buff]
num_needed = [num_1_cost_buff_need, num_2_cost_buff_need]
num_max = [num_1_cost_buff_max, num_2_cost_buff_max]

P_natural_1st = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_1st, num_needed, num_max)
P_natural_2nd = mLib.probability_of_at_least_many_x(num_total, num_wanted, num_draw_2nd, num_needed, num_max)
#Answer: 1st-44.78%, 2nd-55.22%


    #To Generate all permutations of A, B, and C
    perms = product(range(num_draw+1), repeat=num_types)    

    valid_all_perms = [perm for perm in perms]    
    
    # 1st filter is total sum must be num_draw
    valid_perms = [perm for perm in valid_all_perms if sum(perm) == num_draw]        
    
    # 2nd filter is it meets the minimum need requirements
    for i in range(len(num_need_list)):
        valid_perms = [perm for perm in valid_perms if perm[i] >= num_need_list[i]]  
