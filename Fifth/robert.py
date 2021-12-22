import sys
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import io
from sklearn.preprocessing import normalize

plt.rcParams['figure.figsize'] = [10, 5]

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

#computing the magnitude
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
#computing the phase
dft = np.fft.fft2(edged_img)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(np.abs(dft_shift))
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)

#normalization
edged_img_normalized = normalize(edged_img, norm='l2', axis=1, copy=True, return_norm=False)
phase_spectrum_normalized = normalize(magnitude_spectrum, norm='l2', axis=1, copy=True, return_norm=False)

plt.subplot(1,3,1),plt.imshow(img_1,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(edged_img_normalized,cmap = 'gray')
plt.title('Robert'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(phase_spectrum_normalized,cmap = 'gray')
plt.title('phase of Robert'), plt.xticks([]), plt.yticks([])
plt.show()
