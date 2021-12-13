
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

x = np.lcm.reduce(arr)

print(x)
'''


import numpy as np
num = [i for i in range(1, 20 + 1)]
x = np.lcm(num)
print(num)
