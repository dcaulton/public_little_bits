#! /usr/bin/python3


#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# this recurses too deep for 1000 but it works for 100.  Recursion probably wasn't a good fit here, just playing around
#recursive:
#def recur_way(top_of_range):
#    if top_of_range < 3: 
#        return 0
#    if top_of_range % 3 == 0 or top_of_range % 5 == 0:
#        return top_of_range + recur_way(top_of_range - 1)
#    return recur_way(top_of_range - 1)
#print('recursive: {}'.format(recur_way(1000)))


#non-recursive:
sum_nr = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_nr += i
print('non-recursive: {}'.format(sum_nr))
