import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.

plt.plot(x,y)
plt.title("INCOME") 

plt.suptitle("MY SHOP")
plt.show()