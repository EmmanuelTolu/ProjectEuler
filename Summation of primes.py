#This program execute the summation of all prime no btw a range n

num = int(input("Enter n: "))

def primeno(num):

    primelist = []

    for n in range(2,num):

        for i in range(2,n):

            if(n%i==0):

                break

        else:
            primelist.append(n)

    print(sum(primelist))

primeno(num)


#This while loop runs the same
'''
def nextprime(n):
    while True:
        n += 1
        for i in range (2, n):
            if n % i == 0:
                break
        else:
           return n

val, count = 2, 0
primelist = []
while val < num:
    primelist.append(val)
    val = nextprime(val)

print(sum(primelist))
'''
