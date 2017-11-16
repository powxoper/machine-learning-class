
'''
    Generate and plot this dataset (XOR)
    Recall:
    0 XOR 0 = 0
    0 XOR 1 = 1
    1 XOR 0 = 1
    1 XOR 1 = 0
    '''


import matplotlib.pyplot as plt
import numpy as np



# set color of each point by checking its x and y value
def setColor(x, y):
    if (x < 0 and y < 0) or (x > 0 and y > 0): return 'darkblue'
    else: return 'darkred'

# uniform distribution x and y
data_x = np.random.uniform(low = -1.0, high = 1.0, size = 3000)
data_y = np.random.uniform(low = -1.0, high = 1.0, size = 3000)

# use self defined function to set color of each point
colors = list(map(setColor, data_x, data_y))


plt.scatter(data_x, data_y, c=colors, marker = "o", alpha = 0.5) # alpha : how much transparent
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()