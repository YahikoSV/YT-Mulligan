# -*- coding: utf-8 -*-
"""
Goal: To rate your gacha luck
1.) Given a Y chance of getting a limited character
    a.) What is the average number of M pulls of getting the limited character
    b1.) What is your percentile for getting limited characted in X pulls
    b2.) What is your percentile for getting Y limited characters in Y pulls
    c.) Graph the probability distribution of getting limited character over number of pulls.
    d.) Graph the cumulative distribution.
"""


"""
a.) What is the average number of M pulls of getting a limited character.
It's quite easy but you kinda need to stop your approximation if it's too negligible.
So in a coinflip with 1/2 chance of winning
Winners in first flip is 50% (100% of 1/2 chance)
then winners in second flip is 25% (50% of 1/2 chance)
then winners in third flip is 12.5% (25% of 1/2 chance)
and so on...
so there's a summation equation where the

there was an oversight because i used 50%.
i should have used something not equal like 20%

Winners on the first roll = 20% (20% won 80% lost)
Winners on the second roll = 80%*20% (20% won + 16% won 64% lost)
Winners on the thrid roll = 80%*80%*20% (36% won + 12.8% won)

That means if the summation terms is ax^n, a is 20%, x is 80% 
Let's try to simulate the summation
"""

sum_total = 0

a = .06
x = 1 - a
for n in range (0,1000):
    term = a*n*x**n
    sum_total += term
    print(term,sum_total)
    
    
pie = 1
sum_sim = 0
for n in range (0,100):
    winners = pie * a
    pie = pie - winners
    sum_sim += winners
    print(winners,sum_sim)
    
pie = 1
sum_sim = 0
for n in range (0,1000):
    winners = pie * a
    pie = pie - winners
    sum_sim += winners * n
    print(winners,sum_sim)
    
    
"""
Interesting it takes an average 32.3 rolls to win a 3% gacha 
But it takes an average 15.4 rolls to win a 6% gacha (this is 6.4 wins in 100 rolls)
But isnt it that you that better odds than 6% then why so?
Because 100 rolls might not be big enough to convergence to negligible?

let's try 10% rate it converges to 9!!!
"""

sum_total = 0
a = .1
x = 1 - a
for n in range (0,100):
    term = a*n*x**n
    sum_total += term
    print(term,sum_total)

sum_total = 0  #reaches 24.6
a = 1/30
x = 1 - a
for n in range (0,100):
    term = a*n*x**n
    sum_total += term
    print(term,sum_total)
    
sum_total = 0  #reaches 29!
a = 1/30
x = 1 - a
for n in range (0,1000):
    term = a*n*x**n
    sum_total += term
    print(term,sum_total)

sum_total = 0  #reaches 29!
a = 1/2
x = 1 - a
for n in range (0,100):
    term = a*n*x**n
    sum_total += term
    print(term,sum_total)

pie = 1
sum_sim = 0
for n in range (0,100):
    winners = pie * a
    pie = pie - winners
    sum_sim += winners * (n+1)
    print(winners,sum_sim)
    
a = 0.03   
pie = 1
sum_sim = 0
for n in range (0,1000):
    winners = pie * a
    pie = pie - winners
    sum_sim += winners * (n+1)
    print(winners,sum_sim)
    
sum_total = 0  #reaches 29!
a = 0.03
x = 1 - a
for n in range (0,1000):
    term = a*(n+1)*x**n
    sum_total += term
    print(term,sum_total)
    
"""
Realization: there was a mistake..
It was not a anx**n but a(n+1)x**n
That is where the missing 1 comes from incredible tbh.
At the end of the day it's clear that average pulls to win 1 with p chance is 1/p....
So anyways.. what about 

    b1.) What is your percentile for getting limited characted in X pulls
    wait a minute just use the complement of probability of     
"""

probability = .03
pulls = 30
P_get = 1 - (1-probability)**pulls

probability = .03
pulls = 29
P_get2 = 1 - (1-probability)**pulls

probability = .03
pulls = 1
P_get3 = 1 - (1-probability)**pulls

#share of people who got it at 30th pull
probability = .03
pulls = 30
P_get_30 = (1-probability)**(pulls-1)*(probability)

"""
lets try to graph a cumulative distribution graph
"""

import matplotlib.pyplot as plt   
prob = 0.03
x = range(0,100+1)
y = [1 - ( 1 - prob)**i for i in x]
plt.plot(x,y)
plt.show()


"""
What about the percentile of getting 2 limited characters???
Use binomial thereom
(x+y)**n where x+y=1
"""



from math import comb
a = 0.5
b = 1 - a
n = 1
w = 1

prob = 0
for r in range(0,n-w+1):
    fact = comb(n,r)*a**(n-r)*b**(r)
    print(comb(n,r),n,r)
    prob += fact
    
    
a = 0.03
b = 1 - a
n = 30
w = 1

prob = 0
for r in range(0,n-w+1):
    fact = comb(n,r)*a**(n-r)*b**(r)
    print(comb(n,r),n,r)
    prob += fact
    


#prob of 3 3 stars in 100 pulls    
a = 0.03
b = 1 - a
n = 100
w = 3

prob = 0
for r in range(0,n-w+1):
    fact = comb(n,r)*a**(n-r)*b**(r)
    print(comb(n,r),n,r)
    prob += fact
    
    
#prob of 1 rate-up in 200 pulls    
a = 0.06
b = 1 - a
n = 300
w = 4

#x = range(1,n+1)
#y = []
prob = 0
for r in range(0,n-w+1):
    fact = comb(n,r)*a**(n-r)*b**(r)
    #print(comb(n,r),n,r)
    prob += fact
    #y.append(prob)
print(prob)
#plt.plot(x,y)
#plt.show()

"""
~39% cahnce in 70 pulls or less
~50% chance in 100 pulls or less
~75% chance in 200 pulls or less

Now, how to grapht this phenomenon
"""

#graph of probability of getting desired in at least x pulls
a = 0.06
b = 1 - a
n = 200
w = 4

x = range(0,n+1)
y = []
for n in x:
    prob = 0
    for r in range(0,n-w+1):
        fact = comb(n,r)*a**(n-r)*b**(r)
        #print(comb(n,r),n,r)
        prob += fact
        #y.append(n,prob)
    print(n,prob)
    y.append(prob)

plt.plot(x,y)
plt.show()



#graph of probability of getting desired in at least x pulls
a = 0.03
b = 1 - a
n = 400
w = 6

x = range(0,n+1)
y = []
for n in x:
    prob = 0
    for r in range(0,n-w+1):
        fact = comb(n,r)*a**(n-r)*b**(r)
        #print(comb(n,r),n,r)
        prob += fact
        #y.append(n,prob)
    #print(n,prob)
    y.append(prob)

plt.plot(x,y)
plt.axhline(y = 0.5, color = 'r', linestyle = '--', lw = .5) 
plt.axhline(y = 0.25, color = 'g', linestyle = '--', lw = .5) 
plt.axhline(y = 0.75, color = 'b', linestyle = '--', lw = .5) 

i = y.index(next(x for x in y if x > 0.5))
plt.axvline(x = i, color = 'r', linestyle = '--', lw = .5)
j = y.index(next(x for x in y if x > 0.25))
plt.axvline(x = j, color = 'g', linestyle = '--', lw = .5)
k = y.index(next(x for x in y if x > 0.75))
plt.axvline(x = k, color = 'b', linestyle = '--', lw = .5)


plt.show()
print(i,j,k)

plt.title('Probability of getting 6 3 stars in 400 pulls')
plt.plot(x,y, label='probability curve')
plt.hlines(y = 0.5, color = 'r', linestyle = '--', lw = .5, xmin=0, xmax=189, label='50%') 
i = y.index(next(x for x in y if x > 0.5))
plt.vlines(x = i, color = 'r', linestyle = '--', lw = .5, ymin = 0, ymax = 0.5)
plt.xlim(0,)
plt.ylim(0,1)

# place the legend outside
plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')

plt.show()
print(i)


'''
Nice time to make a function for this.
'''


rate_win = 0.03
num_pulls = 400
num_wins = 6 
list_markers = [.01,.25,.50,.75,.99,.98]

def graph_probability_of_winning_x_with_y_pulls(rate_win,num_pulls,num_wins,list_markers):
    rate_lose = 1 - rate_win
    colors = ['b','g','r','c','m','y']
    
    list_pull_num = list(range(0,num_pulls+1))
    list_win_prob = []
    
    for pull_num in list_pull_num:
        win_prob = 0 
        for nth_factor in range(0,pull_num-num_wins+1):
            nth_factor_prob = comb(pull_num,nth_factor)*rate_win**(pull_num-nth_factor)*rate_lose**(nth_factor)
            win_prob += nth_factor_prob
        list_win_prob.append(win_prob)
        
        
    plt.title(f'Probability of {str(num_wins)} wins in {str(num_pulls)} pulls') 
    plt.plot(list_pull_num,list_win_prob, label='probability curve')
    
    
    for marker in range(0,len(list_markers)):
        if list_markers[marker] < list_win_prob[-1]:
            index = list_win_prob.index(next(prob for prob in list_win_prob if prob > list_markers[marker]))
            plt.hlines(y = list_markers[marker], color = colors[marker], linestyle = '--', lw = .5, xmin=0, xmax=index, label=f'{list_markers[marker]}, {index}') 
            plt.vlines(x = index , color = colors[marker], linestyle = '--', lw = .5, ymin=0, ymax = list_markers[marker])  
        
        
    plt.xlim(0,)
    plt.ylim(0,1)
    plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')                
    plt.show()
    return list_pull_num, list_win_prob
        

rate_lose = 1 - rate_win
list_pull_num = list(range(0,num_pulls+1))
list_win_prob = []

for pull_num in list_pull_num:
    print(pull_num)
    win_prob = 0 
    for nth_factor in range(0,pull_num-num_wins+1):
        nth_factor_prob = comb(num_pulls,nth_factor)*rate_win**(num_pulls-nth_factor)*rate_lose**(nth_factor)
        win_prob += nth_factor_prob
        print(nth_factor,nth_factor_prob,win_prob)
        
    list_win_prob.append(win_prob)




rate_win = 0.007
num_pulls = 400
num_wins = 1 
list_markers = [.01,.25,.50,.75,.99,.98]


