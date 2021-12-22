import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from sklearn.preprocessing import normalize

plt.rcParams['figure.figsize'] = [10, 5]

img = cv.imread('Fifth/scenery.jpeg',0)

sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

#magnitude
sobel = np.sqrt( np.square(sobelx) + np.square(sobely))
#phase
dft = np.fft.fft2(sobel)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(np.abs(dft_shift))
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
#normalize
sobel_normalized = normalize(sobel, norm='l2', axis=1, copy=True, return_norm=False)
phase_spectrum_normalized = normalize(magnitude_spectrum, norm='l2', axis=1, copy=True, return_norm=False)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobel_normalized,cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(phase_spectrum_normalized,cmap = 'gray')
plt.title('phase of Sobel'), plt.xticks([]), plt.yticks([])
plt.show()