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
from itertools import combinations
import numpy as np

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

I also realized there are two ways of doing it.
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
Second Row -> Remove duplicates where two fruit As are present
Third Row -> It became complicated because we actually removed all instances where 3 fruit As are present
             Hence we have to add them back
Hmm there might be a pattern tho.
'''  
comb_at_least_1_C = comb(num_A,num_A_need) * comb(num_fruits, num_draw - num_A_need)  \
                    - comb(num_A,2) * comb(num_fruits - 2, num_draw - 2)                           \
                    + comb(num_A,3)
                    
    
'''
Strict Requirement
First row -> Combinations where there is exactly 1 A fruit
Second row -> Combinations where there are exactly 2 A fruits
Third row -> Combinations where there are exactly 3 A fruits
This one is much much easier to follow through
'''
comb_at_least_1_D = comb(num_A,num_A_need) * comb(num_fruits - num_A, num_draw - num_A_need)  \
                    + comb(num_A,2) * comb(num_fruits - num_A, num_draw - 2)                   \
                    + comb(num_A,3)



'''
Let's take it even further because I see a pattern in the first case.
We turn it into 4 draws
And since using paper to count all the combinations is a headache i will now use itertools
'''
num_fruits = 10
num_A      = 4
num_draw   = 4
num_A_need = 1
comb_total = comb(num_fruits,num_draw) #210

basket = ['A1','A2','A3','A4','B1','B2','B3','B4','B5','B6']

comb_list = combinations('AAAABBBBBB',num_draw)


comb_list_array = []
for combo in comb_list:
    #x = ''.join(combo)
    comb_list_array.append(combo)
for hand in range(0,len(comb_list_array)):
    comb_list_array[hand] = ''.join(comb_list_array[hand])
    
    
comb_at_least_1_E = 0   
for hand in range(0,len(comb_list_array)):
    at_least_1 = 1 if comb_list_array[hand].count('A') >= num_A_need else 0
    comb_at_least_1_E = comb_at_least_1_E + at_least_1  #195

'''
The answer is 195 combinations
Now let's try Case B first
4 rows add one at a time, Generalizing the equation
I got it correctly 80 + 90 + 24 + 1 = 195
'''    
comb_at_least_1_F = comb(num_A,num_A_need)       * comb(num_fruits - num_A, num_draw - num_A_need)      \
                    + comb(num_A,num_A_need + 1) * comb(num_fruits - num_A, num_draw - num_A_need - 1)  \
                    + comb(num_A,num_A_need + 2) * comb(num_fruits - num_A, num_draw - num_A_need - 2)  \
                    + comb(num_A,num_A_need + 3) * comb(num_fruits - num_A, num_draw - num_A_need - 3) 
    
'''
Now for the 1st case, it seems like the answer is alternating
So that means we minus at the 4th condition
336 - 168 + 28 - 1 = 195 ! Let's go '
'''
comb_at_least_1_G =   comb(num_A,num_A_need)     * comb(num_fruits - num_A_need, num_draw - num_A_need)          \
                    - comb(num_A,num_A_need + 1) * comb(num_fruits - num_A_need - 1, num_draw - num_A_need - 1)  \
                    + comb(num_A,num_A_need + 2) * comb(num_fruits - num_A_need - 2, num_draw - num_A_need - 2)  \
                    - comb(num_A,num_A_need + 3) * comb(num_fruits - num_A_need - 3, num_draw - num_A_need - 3)     
    
'''
We can turn this into a summation and prove that they are equal but I'm not insane enough to do it so
I will continue by making a code out of this generalization.
'''

def probability_of_at_least_x(num_total, num_wanted, num_needed = 1, num_draw = 1):
    comb_total = comb(num_total,num_draw)
    comb_want  = 0
    for i in range(0,num_draw):
        x = comb(num_wanted, num_needed + i) * comb(num_total - num_wanted, num_draw - num_needed - i)
        print(x)
        comb_want = comb_want + x
    return comb_want, comb_total, comb_want / comb_total

'''
Case A time
'''
def probability_of_at_least_y(num_total, num_wanted, num_needed = 1, num_draw = 1):
    comb_total = comb(num_total,num_draw)
    comb_want  = 0
    for i in range(0,num_draw):
        x = (-1)**(i) * comb(num_wanted, num_needed + i) * comb(num_total - num_needed - i, num_draw - num_needed - i)
        print(x)
        comb_want = comb_want + x
    return comb_want, comb_total, comb_want / comb_total    

'''
What's interesting in this format of Case B is that you can solve problems of the probability of
getting exactly x amount of A fruits, or in a range of x to y A fruits. 
For the continuation of the script we will be solely using Case B
To take account of a range we edit for an upper limit num_max_needed:
'''

def probability_of_at_least_x(num_total, num_wanted, num_needed = 1, num_draw = 1, num_max_needed = -1):
    num_max_needed = num_draw if  num_max_needed == -1 else num_max_needed
    comb_total = comb(num_total,num_draw)
    comb_want  = 0
    for i in range(0,num_max_needed - num_needed + 1):
        x = comb(num_wanted, num_needed + i) * comb(num_total - num_wanted, num_draw - num_needed - i)
        print(i,x)
        comb_want = comb_want + x
    return comb_want, comb_total, comb_want / comb_total

    
num_fruits = 10
num_A      = 4
num_draw   = 4
num_A_need = 2
num_A_max  = 3    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    