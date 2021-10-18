#This program shows the largest palindrome of a 3 digit
data1 = data2 = range(999, 100, -1)
pal = []

def largest_palindrome_3digit(data1, data2):
    for i in data1:
        for j in data2:
            l = str(i * j)
            if l == l[::-1]:
                pal.append(int(l))
    print(max(pal))
largest_palindrome_3digit(data1, data2)
