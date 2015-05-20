#! /usr/bin/python3

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#DMC NOTE - theres a gotcha here.  
## When I'm looking at x[-1], it's the last element of the array
## When I do the slice x[1:-1] it takes the slice up to the SECOND TO LAST ELEMENT of the array
## so for 54321, x[-1] is 1, x[1:-1] is 432
def is_a_pal(x):
    if len(x) < 2:
        return True
    if x[0] == x[-1]:
        return is_a_pal(x[1:-1])
    return False

top_of_range = 1000
products = {}
for i in range(top_of_range, 1, -1):
    for j in range(top_of_range, 1, -1):
        products[i*j] = True

for i in reversed(sorted(products.keys())):
    if is_a_pal(str(i)):
        print('the largest palindrome for top of range {} is {}'.format(top_of_range, str(i)))
        exit(0)
