# -*- coding: utf-8 -*-
"""
Databse of mulligan functions
"""

from math import comb
from itertools import product

def probability_of_at_least_x(num_total, num_wanted, num_needed = 1, num_draw = 1, num_max_needed = -1):
    num_max_needed = num_draw if  num_max_needed == -1 else num_max_needed
    comb_total = comb(num_total,num_draw)
    comb_want  = 0
    for i in range(0,num_max_needed - num_needed + 1):
        x = comb(num_wanted, num_needed + i) * comb(num_total - num_wanted, num_draw - num_needed - i)
        comb_want = comb_want + x
        
    return comb_want, comb_total, comb_want / comb_total



def probability_of_at_least_many_x(num_total, num_want_list, num_draw = -1, num_need_list = -1, num_max_need_list = -1):
    
    #To fill-in the arguments that are not needed
    #You need num_need_list for minimum required draw and num_max_need_list for maximum outcome
    num_need_list = [1 for need in num_want_list] if num_need_list == -1 else num_need_list
    num_draw = sum(num_need_list) if num_draw == -1 else num_draw    
    num_max_need_list = [num_draw for max_need in num_want_list] if num_max_need_list == -1 else num_max_need_list
    
    
    comb_total = comb(num_total,num_draw)
    num_types = len(num_need_list) + 1   #add 1 as left-overs
    
          
   

    #To Generate all permutations of A, B, and C
    perms = product(range(num_draw+1), repeat=num_types)    

    valid_all_perms = [perm for perm in perms]    
    
    # 1st filter is total sum must be num_draw
    valid_perms = [perm for perm in valid_all_perms if sum(perm) == num_draw]        
    
    # 2nd filter is it meets the minimum need requirements
    for i in range(len(num_need_list)):
        valid_perms = [perm for perm in valid_perms if perm[i] >= num_need_list[i]]         
     
    # Calculate all the occurances per combination
    comb_want_total  = 0
    for i in range(len(valid_perms)):
        comb_perm_total = 1
        for j in range(len(valid_perms[i])):
            if j != len(valid_perms[i]) - 1:
                comb_perm_total = comb_perm_total * comb(num_want_list[j],valid_perms[i][j])
            else: 
                comb_perm_total = comb_perm_total * comb(num_total - sum(num_want_list),valid_perms[i][j])            
        comb_want_total = comb_want_total + comb_perm_total              
    
    return comb_want_total, comb_total, comb_want_total / comb_total    