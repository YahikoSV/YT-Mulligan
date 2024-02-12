# -*- coding: utf-8 -*-
"""
Step 1: understand Combinations
1.) Probability of Getting   1 A fruit in z fruits in 1 try
2.) Probability of Getting   at least 1 A fruit in z fruits in y tries

3.1) Probability of Getting  exactly  x A fruit in z fruits in y tries
3.2) Probability of Getting  at least x A fruit in z fruits in y tries

4.) Probability of Getting  1 A fruit and 1 B fruit in z fruits in y tries
5.) Probability of Getting  x1 A fruit and x2 B fruit in z fruits in y tries

"""

from math import comb
import itertools


'''
1.) There are 10 fruits, and 4 of them are A fruit. What is the probability of getting A fruit after 1 draw.

P_step_1 = number of combs you get A fruit / number of combninations you get a fruit.
'''
num_fruits = 10
num_A      = 4
num_draw   = 1

P_step_1 = num_A / num_fruits

#Combinatorics
P_step_1_com = comb(num_A,num_draw) / comb(num_fruits,num_draw)




'''
2.) There are 10 fruits, and 4 of them are A fruit. What is the probability of getting A fruit after 2 draws.

P_step_2 = number of combs you get A fruit / number of combninations you get a fruit.

This time you have 2 tries thus we use the compliment where we calculate the probability where you get no 
A fruit at all

'''

num_fruits = 10
num_A      = 4
num_draw   = 2

P_step_2 =  1 - ((num_fruits - num_A) / num_fruits)**num_draw

'''
something's not right
this is with replacement
you need a probability without replacement
'''

num_nonA = num_fruits - num_A
P_step_2B = 1
for i in range(0,num_draw):
    P_step_2B = P_step_2B * ((num_nonA - i)/(num_fruits - i))
    
P_step_2B = 1 - P_step_2B

P_step_2A = 1 - (((num_fruits - num_A) / num_fruits) * ((num_fruits - num_A - 1) / (num_fruits - 1)))


'''
To get it's combinatorics you need to say that you got 1 A fruit already and say that the rest are optional
But also you have to take the combination 
comb(num_A,num_A_need) * comb(num_fruits - num_A_need, num_draw - num_A_need)

'''
#Combinatorics
num_A_need = 1
P_step_2_com = comb(num_A,num_A_need) * comb(num_fruits - num_A_need, num_draw - num_A_need) / comb(num_fruits,num_draw)

'''
something is not right
did it hands on i got 2/3 so that's the correct answer
i realized that something got doubled, the case where you get 2 A fruits instead of 1 A.

I also realized there are two ways of doin it.
Either get the combination of the least requirement (like the one above) and subtract the extras
Or get the combinations of the strict requirement and add the extras
'''    

#Extras here are the case when 2 A fruits were drawn
extra = comb(num_A,num_draw) 

#Least requirement
comb_at_least_1_A = comb(num_A,num_A_need) * comb(num_fruits - num_A_need, num_draw - num_A_need) - extra
#Strict Requirement
comb_at_least_1_B = comb(num_A,num_A_need) * comb(num_fruits - num_A, num_draw - num_A_need) + extra    
    
P_step_2_com = comb_at_least_1_A  / comb(num_fruits,num_draw)


'''
let's try make it a bit complicated where instead of 2 draws. We turn it to 3 draws.
We are going to use both methods

We have to figure out how to get 5/6
'''    
num_fruits = 10
num_A      = 4
num_draw   = 3
num_A_need = 1
comb_total = comb(num_fruits,num_draw) #120
'''
A. Least Requirement
First row -> Least req count  
Second Row -> 
'''  
comb_at_least_1_C = comb(num_A,num_A_need) * comb(num_fruits - num_A_need, num_draw - num_A_need)  \
                    - comb(num_A,2) * comb(num_fruits - 2, num_draw - 2)
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    