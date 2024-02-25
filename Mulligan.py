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

from math import comb, perm
from itertools import combinations
from itertools import permutations
from itertools import product
import numpy as np

'''
02/18/2024
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
                    - comb(num_A,2) * comb(num_fruits - 2, num_draw - 2)                \
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
    
    
    
    
'''
02/25/2024
1-3 is done time to solve for 4-5 
4.) There are 10 fruits, and 4 of them are A fruit and 3 of them are B fruit
    What is the probability of getting both A fruit and B fruit after 2 draws.

Let's try simulating it
'''   

num_fruits = 10
num_A      = 4
num_A_need = 1
num_B      = 3
num_B_need = 1
num_draw   = 2
comb_list = combinations('AAAABBBCCC',num_draw)


comb_list_array = []
for combo in comb_list:
    #x = ''.join(combo)
    comb_list_array.append(combo)
for hand in range(0,len(comb_list_array)):
    comb_list_array[hand] = ''.join(comb_list_array[hand])
    
    
comb_at_least_1_E = 0   
for hand in range(0,len(comb_list_array)):
    at_least_1 = 1 if comb_list_array[hand].count('A') >= num_A_need and comb_list_array[hand].count('B') >= num_B_need else 0
    comb_at_least_1_E = comb_at_least_1_E + at_least_1   
    
result = comb_at_least_1_E / len(comb_list_array)    # 12/45 or .266
    
'''
Hypothesis
it is the same as probability of getting A * prbability of getting B
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
num_A_need = 1
num_B      = 3
num_B_need = 1
num_draw   = 2

A_prob = probability_of_at_least_x(num_fruits, num_A, num_A_need, num_draw, 1)
B_prob = probability_of_at_least_x(num_fruits, num_B, num_B_need, num_draw, 1)    
prob_AB = A_prob[2] * B_prob[2]    # .2488 which is different why? idk

'''
You can treat the calculation as
comb(A) * comb(B) * comb(left)
'''
AB_comb = comb(num_A,num_A_need) * comb(num_B,num_B_need) * comb(num_fruits-num_A-num_B,num_draw - num_A_need - num_B_need)
    
    
'''
But what happens if we draw 3 this time?
from AB only to ABC, AAB, ABB
'''    
    
num_fruits = 10
num_A      = 4
num_A_need = 1
num_B      = 3
num_B_need = 1
num_draw   = 3
comb_list = combinations('AAAABBBCCC',num_draw)


comb_list_array = []
for combo in comb_list:
    #x = ''.join(combo)
    comb_list_array.append(combo)
for hand in range(0,len(comb_list_array)):
    comb_list_array[hand] = ''.join(comb_list_array[hand])
    
    
comb_at_least_1_E = 0   
for hand in range(0,len(comb_list_array)):
    at_least_1 = 1 if comb_list_array[hand].count('A') >= num_A_need and comb_list_array[hand].count('B') >= num_B_need else 0
    comb_at_least_1_E = comb_at_least_1_E + at_least_1   
    
AB_comb_2 = comb_at_least_1_E   #66

'''
Split into 3 cases
1st line is ABC Case
2nd line is AAB Case
3rd line is ABB Case
'''
AB_comb_2 =   comb(4,2) * comb(3,1) * comb(3,0) \
            + comb(4,1) * comb(3,2) * comb(3,0) \
            + comb(4,1) * comb(3,1) * comb(3,1) 

'''
So how do we code this abomination?
It's easy if there's only a max of 2 then that means you only need 2 loops
But if you have n many conditions. it's not feasibile to do n many loops
There must be a way to iterate all combinations and pick the ones that meet our conditions

I ask chatgpt 3.5
They answer the gave me was permutations and it makes sense since order matters
but ofc you have to still put the sum condition at the end.
'''    

num_types = 3

# Define the possible integers A, B, and C
integers = range(10+1) 
    
#Total permuations
perms_total = len(integers)**(num_types) 

# Generate all permutations of A, B, and C
perms = product(integers, repeat=num_types)    
    
# Filter permutations where the sum equals 10
valid_perms = [perm for perm in perms if sum(perm) == 10]    

#Count valid perms
valid_perms_total = len(valid_perms) #66


'''
for the case above we have 3 types of fruits meaning the range of each count is 0 to 3
'''

num_types = 3
num_draw  = 3
# Define the possible integers A, B, and C
integers = range(num_draw+1)    
    
#Total permuations
perms_total = len(integers)**(num_types) 

# Generate all permutations of A, B, and C
perms = product(integers, repeat=num_types)    

valid_all_perms = [perm for perm in perms]
    

# Filter permutations where the sum equals 10
valid_perms = [perm for perm in valid_all_perms if sum(perm) == num_draw]    
#Count valid perms
valid_perms_total = len(valid_perms) #10

#but if we want to add the other conditions of 1A + 1B]
valid_perms_2 = [perm for perm in valid_all_perms if sum(perm) == num_draw and perm[0] >= num_A_need and perm[1] >= num_B_need]    
valid_perms_total_2 = len(valid_perms_2) #3


    
'''
Since tuples are iterable, we can just practically plug in each possiblity in 1 for loop
and we done we kinda solved 4 and 5 in this case and even the case for multiple fruit conditions!

The to make a function for it
For the input i have to assume it has to be a list now to accomodate all the possible scenarios

num_total  = (number) total number of objects
num_wanted = (list)   number of desired objects in total per type
num_need   = (list)   number of desired objects needed per type
num_draw   = (number) total number of draws
num_max_needed = (list)  max number of desired objects needed per type


'''

num_total = 10
num_A      = 4
num_A_need = 1
num_B      = 3
num_B_need = 1
num_draw   = 3

num_want_list = [num_A,num_B]
num_need_list   = [num_A_need,num_B_need]

def probability_of_at_least_many_x(num_total, num_want_list, num_draw = -1, num_need_list = -1, num_max_need_list = -1):
    
    #To fill-in the arguments that are not needed
    #You need num_need_list for minimum required draw and num_max_need_list for maximum outcome
    num_need_list = [1 for need in num_want_list] if num_need_list == -1 else num_need_list
    num_draw = sum(num_need_list) if num_draw == -1 else num_draw    
    num_max_need_list = [num_draw for max_need in num_want_list] if num_max_need_list == -1 else num_max_need_list
    
    
    comb_total = comb(num_total,num_draw)
    num_types = len(num_need_list) + 1   #add 1 as left-overs
    
          
    #Total permutations with repetition
    perms_total = (num_draw+1)**(num_types)     

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
        #print("i",i)
        comb_perm_total = 1
        for j in range(len(valid_perms[i])):
            #print("j",j)        
            if j != len(valid_perms[i]) - 1:
                #print('comb',comb(num_want_list[j],valid_perms[i][j]))
                comb_perm_total = comb_perm_total * comb(num_want_list[j],valid_perms[i][j])
            else: 
                #print('comb',comb(num_total - sum(num_want_list),valid_perms[i][j]))
                comb_perm_total = comb_perm_total * comb(num_total - sum(num_want_list),valid_perms[i][j])            
        #print('sum_comb',comb_perm_total)
        comb_want_total = comb_want_total + comb_perm_total 
        
    #print('sum_perm',comb_want_total)       
    
    return comb_want_total, comb_total, comb_want_total / comb_total     
            
'''
And we are done let's do an example
'''

num_total = 12
num_draw  = 5
num_want_list = [4,4,4]
num_need_list = [2,1,1]   
    
answer = probability_of_at_least_many_x(num_total, num_want_list, num_draw, num_need_list)
    
'''
Let's simulate it the long way
'''

num_total = 12
num_draw = 5
num_want_list = [4,4,4]
num_need_list = [2,1,1]   
num_id_list   = ['A','B','C']
comb_list = combinations('AAAABBBBCCCC',num_draw)


comb_list_array = []
for combo in comb_list:
    #x = ''.join(combo)
    comb_list_array.append(combo)
for hand in range(0,len(comb_list_array)):
    comb_list_array[hand] = ''.join(comb_list_array[hand])
    
    
comb_want = 0   
for hand in range(0,len(comb_list_array)):
    at_least_1 = 1 if comb_list_array[hand].count(num_id_list[0]) >= num_need_list[0] \
                  and comb_list_array[hand].count(num_id_list[1]) >= num_need_list[1] \
                  and comb_list_array[hand].count(num_id_list[2]) >= num_need_list[2]     else 0
    comb_want = comb_want + at_least_1   #352
    
answer_2 = (comb_want,len(comb_list_array),comb_want/len(comb_list_array))    
    