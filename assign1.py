import numpy as np
import matplotlib.pyplot as plt
import time
import os

path_row = ['books', 'prince.txt']#[]
message = 'Insert input'

"""
print(message)
while True:
    if input() == '':
        break
    else:
        path_row.append(input())
"""

path = os.path.join(*path_row)

with open(path, 'r') as file:
    prince = file.read().split()

hist = dict.fromkeys(prince, 0)

for word in prince:
    hist[word] += 1

num_words = len(hist.values())
print(num_words)

words_ord = list(hist.values())
words_ord.sort()

plt.figure(figsize=(10,4))
plt.plot(range(num_words), words_ord, color='black', marker='.', linestyle='-')
plt.show()
