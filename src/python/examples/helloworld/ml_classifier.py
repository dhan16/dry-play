"""
https://www.quora.com/Who-can-show-me-a-piece-of-machine-learning-code-and-explain-in-short-what-it-does
"""

import numpy as np  # library for basic matrix calculation
import matplotlib.pyplot as plt  # library for basic plotting


def min_distance(group, point):
    diff = group - point
    return np.min(np.sum(diff**2, 0))


N = 5
stars = np.random.rand(2, N)
triangles = .5 + np.random.rand(2, N)

plt.scatter(stars[0], stars[1], c='r', marker='*', s=100)
plt.scatter(triangles[0], triangles[1], c='b', marker='^', s=100)
# plt.show()

new_point = np.random.rand(2, 1)
plt.scatter(new_point[0], new_point[1], c='k', marker='o', s=100)
plt.show()

cluster = 'stars' if min_distance(stars, new_point) < min_distance(triangles, new_point) else 'triangles'
print(cluster)
