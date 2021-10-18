#This is for the 10001st prime

def nextprime(n):
    while True:
        n += 1
        for i in range (2, n):
            if n % i == 0:
                break
        else:
           return n

val, count = 1, 0
primelist = []
while count < 10001:
    primelist.append(val)
    val = nextprime(val)
    count += 1

print(val)
