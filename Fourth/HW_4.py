from PIL import Image, ImageOps
from scipy import ndimage
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import shannon_entropy as entropy

# def entropy(signal):
#         '''
#         function returns entropy of a signal
#         signal must be a 1-D numpy array
#         '''
#         lensig=signal.size
#         symset=list(set(signal))
#         numsym=len(symset)
#         propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
#         ent=np.sum([p*np.log2(1.0/p) for p in propab])
#         return ent

#1
numbers = [ 15, 20, 8, -8, -10]
image = np.zeros(shape=(256,256))

for i in range(256):
    for j in range(256):
        rand_num = np.random.randint(0, 5)
        image[i][j] = numbers[rand_num]

print(f'Entropy before zeroing: {entropy(image)}')

for i in range(0,256,16):
    for j in range(0,256,16):
      for k in range(121):
          rand1 = np.random.randint(0, 16)
          rand2 = np.random.randint(0, 16)
          image[rand1+i][rand2+j] = 0

print(f'Entropy after zeroing: {entropy(image)}')

#2
print(f'Entropy before summation: {entropy(image)}')
newImage = Image.open('Fourth/naruto.png').convert('L')
newImage.save('Fourth/naruto_gry.png')
newImage = newImage.resize((256, 256))
newImage = np.array(newImage)
twoImage = newImage + image
twoImage = np.where(twoImage<0,0,twoImage)
print(f'Entropy after summation: {entropy(twoImage)}')

#3
kernel = np.ones((5,5),np.float32)/25
mean = cv2.filter2D(twoImage,-1,kernel)
print(f'Mean entropy: {entropy(mean)}')
median = ndimage.median_filter(twoImage, 5)
print(f'Median entropy: {entropy(median)}')
fig0 = plt.figure(figsize=(12,5))
ax1 = fig0.add_subplot(1,3,1)
ax1.imshow(twoImage)
ax1.set_title('Noisy')
ax1.axis('off')
ax1 = fig0.add_subplot(1,3,2)
ax1.imshow(mean)
ax1.set_title('mean')
ax1.axis('off')
ax2 = fig0.add_subplot(1,3,3)
ax2.imshow(median)
ax2.set_title('median')
ax2.axis('off')
plt.show()
inverted_mean = Image.fromarray(mean)
inverted_mean.save('Fourth/naruto_mean.png')

# #4
# mean2 = cv2.imread('Fourth/naruto_mean.png', 0)
# first_derivative_base = cv2.Sobel(twoImage, cv2.CV_32F, 1, 0, ksize=3)
# first_derivative_mean = cv2.Sobel(mean2, cv2.CV_32F, 1, 0, ksize=3)
# first_derivative_median = cv2.Sobel(median, cv2.CV_32F, 1, 0, ksize=3)
# fig1 = plt.figure(figsize=(12,6))
# ax3 = fig1.add_subplot(1,3,1)
# ax3.imshow(first_derivative_base)
# ax3.set_title('first_derivative_base')
# ax3.axis('off')
# ax4 = fig1.add_subplot(1,3,2)
# ax4.imshow(first_derivative_mean)
# ax4.set_title('first_derivative_mean')
# ax4.axis('off')
# ax4 = fig1.add_subplot(1,3,3)
# ax5.imshow(first_derivative_median)
# ax5.set_title('first_derivative_median')
# ax5.axis('off')
# plt.show()

# #5
# # image_sec_derivative = laplace(twoImage)