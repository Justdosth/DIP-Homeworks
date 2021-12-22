# import libraries
import numpy as np
import matplotlib.pyplot as plt

# line 1 points
x1 = np.linspace(0,256,8)
y1 = x1*(6+6+2) + x1*(5+5+1)
# plotting the line 1 points 
plt.plot(x1, y1, label = "Sobel")

# line 2 points
x2 = np.linspace(0,256,8)
y2 = x2*9 + x2*8
# plotting the line 2 points 
plt.plot(x2, y2, label = "Laplacian")

plt.xlabel('WxH of image')
# Set the y axis label of the current axis.
plt.ylabel('number of computation')
# Set a title of the current axes.
plt.title('Computation cost')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()