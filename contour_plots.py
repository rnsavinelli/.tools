import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1/4) - (x/2) + (y/3)

x, y = np.meshgrid(np.arange(-10, 10, 0.2), np.arange(-10, 10, 0.2))

plt.title('Contour Plot')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.contour(x, y, f(x, y), range(-10, 10))

plt.show()
