# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# img = cv.imread('Fifth/punch.jpeg',0)
# laplacian = cv.Laplacian(img,cv.CV_64F)
# sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
# sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()

import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('Fifth/punch.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
phase_spectrum = np.angle(dft_shift)

ax1 = plt.subplot(1,2,1)
ax1.imshow(img, cmap='gray')

ax2 = plt.subplot(1,2,2)
ax2.imshow(phase_spectrum, cmap='gray')

plt.show()