import math
import numpy as np
import matplotlib.pyplot as plt

def xMin(x1, x2):
	return x1 <= x2

def xMax(x1, x2):
	return x1 >= x2

def yMin(points):
	return reversed(range(len(points)))

def yMax(points):
	return range(len(points))

# Fixing random state for reproducibility
np.random.seed(87656)

N = 20
x = np.random.randint(100, size=(1, 20))[0]
y = np.random.randint(100, size=(1, 20))[0]

xDom = 0
yDom = 1

xCase = xMax if xDom > 0 else xMin
yCase = yMax if yDom > 0 else yMin

colors = ['red']*N

front = []

points = sorted(zip(x, y, colors), key=lambda x:x[1])

front_point = points[0] if yDom > 0 else points[-1]

for i in yCase(points):
	if xCase(points[i][0], front_point[0]):
		front_point = points[i]
		temp = list(points[i])
		temp[2] = 'blue'
		points[i] = tuple(temp)
		front.append(tuple(temp))

points = zip(*points)
x, y, colors = points

plt.scatter(x, y, s=25, c=colors, alpha=0.5)

front = zip(*front)
x, y, colors = front

plt.plot(x, y)
plt.show()