#this is for sum of squares
#lum, count = [], 0
'''
def sum_of_squares(n):
    lum, count = [], 0
    num = [i for i in range(1, n+1)]
    nm = sum(num)
    nm = nm ** 2
    for i in num:
           i = i ** 2
           count = i + 1
           lum.append(i)
    lum = sum(lum)
    print(nm - lum)

sum_of_squares(100)
'''


n = int(input("Enter n: "))
def my_func(n):
    num = range(n+1)
    sum_of_squares = sum([i ** 2 for i in num])
    square_of_sum = sum(num) ** 2

    return square_of_sum - sum_of_squares

result = my_func(n)
print(result)
