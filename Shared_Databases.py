# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:45:34 2024

@author: admin
"""

import urllib.request
import json
#Identify Class of Card based on number assigned in card no.
def identifyClass(number):
    Classes = {  0 : 'Neutral'
                ,1 : 'Forestcraft'
                ,2 : 'Swordcraft'
                ,3 : 'Runecraft'
                ,4 : 'Dragoncraft'
                ,5 : 'Shadowcraft'
                ,6 : 'Bloodcraft'
                ,7 : 'Havencraft'
                ,8 : 'Portalcraft'}
    return Classes[number]    

#Identify Type of Card based on number assigned in card no.
def identifyCardType(number):
    CardType = { 1 : 'Follower'
                ,2 : 'Amulet'
                ,3 : 'Countdown Amulet'
                ,4 : 'Spell'}
    return CardType[number]  
    

def createLinkFromCode(deck_code, lang = 'en', mode = 'R', valid_input = False):
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