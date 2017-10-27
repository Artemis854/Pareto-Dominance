import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(34124)

N = 20
x = np.random.rand(N)
y = np.random.rand(N)
colors = ['red']*N

x = [ int(i*150) for i in x ]
y = [ int(i*150) for i in y ]

front = []

points = sorted(zip(x, y, colors), key=lambda x:x[1], reverse=True)

front_point = points[0]

for i in range(len(points)):
	if points[i][0] <= front_point[0]:
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
