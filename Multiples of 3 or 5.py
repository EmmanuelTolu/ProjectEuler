'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
#First Solution
'''
my3 = [x for x in range(0, 1000, 3)]
my5 = [y for y in range(0, 1000, 5)]
new = set(my5) - set(my3)
my3.extend(new)
Sum = sum(my3)
print(Sum)
'''

#Second Solution

def myfunction(n):
    mult_3_5 = [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
    print(sum(mult_3_5))
myfunction(1000)


    
