import numpy as np
import cv2 as cv
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import io
from sklearn.preprocessing import normalize

plt.rcParams['figure.figsize'] = [10, 5]

#robert
roberts_cross_v = np.array( [[ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

roberts_cross_h = np.array( [[ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )

img_1 = io.imread('Fifth/scenery.jpeg')

img = img_1.astype('float64')
gray_img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
gray_img /= 255

vertical = ndimage.convolve( gray_img, roberts_cross_v )
horizontal = ndimage.convolve( gray_img, roberts_cross_h )

#sobel
sobelx = cv.Sobel(gray_img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(gray_img,cv.CV_64F,0,1,ksize=5)
#computing the magnitude
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
sobel = np.sqrt( np.square(sobelx) + np.square(sobely))
#computing the phase
dft0 = np.fft.fft2(edged_img)
dft_shift0 = np.fft.fftshift(dft0)
magnitude_spectrum0 = 20*np.log(np.abs(dft_shift0))
magnitude_spectrum0 = np.asarray(magnitude_spectrum0, dtype=np.uint8)
dft1 = np.fft.fft2(sobel)
dft_shift1 = np.fft.fftshift(dft1)
magnitude_spectrum1 = 20*np.log(np.abs(dft_shift1))
magnitude_spectrum1 = np.asarray(magnitude_spectrum1, dtype=np.uint8)

#normalization
robert_normalized = normalize(edged_img, norm='l1', axis=1, copy=True, return_norm=False)
phase_robert_normalized = normalize(magnitude_spectrum0, norm='l2', axis=1, copy=True, return_norm=False)
sobel_normalized = normalize(sobel, norm='l1', axis=1, copy=True, return_norm=False)
phase_sobel_normalized = normalize(magnitude_spectrum1, norm='l2', axis=1, copy=True, return_norm=False)

plt.subplot(2,3,1),plt.imshow(img_1,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(robert_normalized,cmap = 'gray')
plt.title('Robert'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(phase_robert_normalized,cmap = 'gray')
plt.title('phase of Robert'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(sobel_normalized,cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(phase_sobel_normalized,cmap = 'gray')
plt.title('phase of Sobel'), plt.xticks([]), plt.yticks([])
plt.show()
