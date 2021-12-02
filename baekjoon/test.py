from matplotlib import patches
import matplotlib.pyplot as plt
import random
steps = 10
nums = range(10)
color_set = [
    'red',
    'green',
    'blue',
    'red',
    'green',
    'blue',
    'red',
    'green',
    'blue',
    'red'
]

data = []
for s in range(steps):
    data.append([])
    for n in nums:
        data[s].append(random.randint(0, 1))

import numpy as np
a = np.array(data)
print(a.shape)

plt.plot()
for x, d in enumerate(data):
    for y, spike in enumerate(d):
        height = 0
        if spike > 0:
            height = 0.5
        plt.vlines(x, y, y+height, linewidth=2,color=color_set[y])


#rate = list(map(lambda x: x), 1)

plt.show()
print(*data)