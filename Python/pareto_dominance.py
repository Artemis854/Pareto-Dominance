import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(928471278)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = ['red']*50

x = [ int(i*30) for i in x ]
y = [ int(i*30) for i in y ]

points = sorted(zip(x, y, colors), key=lambda x:x[1])

front_point = points[0]

for i in range(len(points)):
	if points[i][0] >= front_point[0]:
		front_point = points[i]
		temp = list(points[i])
		temp[2] = 'blue'
		points[i] = tuple(temp)

points = zip(*points)

x, y, colors = points

plt.scatter(x, y, s=5, c=colors, alpha=0.5)
plt.show()
