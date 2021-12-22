import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = [10, 5]

img = cv.imread('Fifth/scenery.jpeg',0)
#laplace
laplacian = cv.Laplacian(img,cv.CV_64F,ksize=3)
#sobel two times
sobelx1 = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobely1 = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
sobel1 = np.sqrt( np.square(sobelx1) + np.square(sobely1))
sobelx2 = cv.Sobel(sobel1,cv.CV_64F,1,0,ksize=3)
sobely2 = cv.Sobel(sobel1,cv.CV_64F,0,1,ksize=3)
sobel2 = np.sqrt( np.square(sobelx2) + np.square(sobely2))

#changing before adding
Laps = laplacian*100.0/np.amax(laplacian)
better_with_laplacian = abs(img + Laps) #Add negative Laplacian to the original image
better_with_laplacian *= 255.0/np.amax(better_with_laplacian)
Sob = sobel2*100.0/np.amax(sobel2)
better_with_sobel = abs(img + Sob) #Add negative Laplacian to the original image
better_with_sobel *= 255.0/np.amax(better_with_sobel)


plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(sobel2,cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(better_with_laplacian,cmap = 'gray')
plt.title('Enhanced with laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(better_with_sobel,cmap = 'gray')
plt.title('Enhanced with sobel'), plt.xticks([]), plt.yticks([])
plt.show()