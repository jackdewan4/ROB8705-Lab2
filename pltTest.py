import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

gauss = cv.getGaussianKernel(31, 5)
gaus = np.outer(gauss,gauss)
#Surface plot of Gaussian Filter
n = 31
# fig = plt.figure()
# ax = fig.add_subplot(1,2,1, projection='3d')

x = np.arange(0, n, 1)
y = np.arange(0, n, 1)
X, Y = np.meshgrid(x, y)
Z = gaus.flatten()
plt.plot(X, Y, gaus, cmap='viridis', projection='3d')
plt.show()

# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2*np.pi*t)
# plt.plot(t, s)
# plt.show()