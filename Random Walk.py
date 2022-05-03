import numpy as np
import random
import matplotlib.pyplot as plt

n = 1000 #set the number of movements

x = np.zeros(n)
y = np.zeros(n)

for i in range(1,n):
    val = random.randint(1,4)
    if val == 1:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    if val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    if val == 3:
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
    if val == 4:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
        
plt.figure()
plt.plot(x, y)
plt.plot([0, x[n-1]], [0, y[n-1]], 'yo', linestyle="--")

