import numpy as np
import matplotlib.pyplot as plt


# a = np.array([
#     [1, 2, 3],
#     [4, 50, 6],
#     [7, 8, 90],
# ])
# print(a)
# plt.imshow(a, interpolation='None')
# plt.imshow(a)

# x = np.arange(0, 3.14/2, 0.1)
# y = np.sin(x)
# print(x)
# print(y)
# plt.plot(x,y)
#
a = np.random.power(1, size=(110,100))
print(a)
plt.imshow(a, cmap='copper')

plt.show()


