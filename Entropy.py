r = int(input('Please enter number of red balls in the bucket: '))
b = int(input('Please enter number of blue balls in the bucket: '))

import math
m = (-1 * r / (r+b))
n = (-1 * b / (r+b))
l1 = math.log(-m, 2)
l2 = math.log(-n, 2)
entropy = (m * l1) + (n * l2)

print('Entropy:', entropy)
