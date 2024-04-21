import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker="|", linestyle='dashdot', c = '#4CAF50',linewidth = '10.5')
plt.show()

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

