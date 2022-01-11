colors = int(input('How many different ball colors are there in your bucket? '))

counts = []
for i in range(1, colors + 1):
    count = int(input('Please enter number of color ' + str(i) + ' balls in the bucket: '))
    counts.append(count)

# print(counts)

probs = []
for i in counts:
    prob = i / sum(counts)
    probs.append(prob)

# print(probs)

import math
entropy = 0
for j in probs:
    l = -j * math.log(j, 2)
    entropy = entropy + l

print('Entropy:', entropy)
