from PIL import Image, ImageOps
import cv2
import numpy as np
from matplotlib import pyplot as plt

myImage = Image.open('anime.jpg').convert('L')
myImage = myImage.resize((256, 256))
myImage.save('Third/anime_gry.jpg')
myImage_array_original = np.array(myImage)
myImage_array = myImage_array_original.copy()

#alef
for i, lst in enumerate(myImage_array):
    for j, item  in enumerate(lst):
        shrinked_value = round(
            (
                (
                    (180-70)/(255-0)
                )
                    *(item-0)
                )
                +70
            )
        myImage_array[i][j] = shrinked_value

myImage_array_sh = myImage_array.copy()
image_shrinked = Image.fromarray(myImage_array)
image_shrinked.save('Third/anime_shrink.jpg')

#be
for i, lst in enumerate(myImage_array):
    for j, item  in enumerate(lst):
        stretched_value = round(
            (item-70)/(180-70)*255
        )
        myImage_array[i][j] = stretched_value

image_stretched = Image.fromarray(myImage_array)
image_stretched.save('Third/anime_stretch.jpg')

#je
img = cv2.imread('Third/anime_shrink.jpg',0)
equ = cv2.equalizeHist(img)
cv2.imwrite('Third/anime_equilized.jpg', equ)

#de
def entropy(im):
    # Compute normalized histogram -> p(g)
    p = np.array([(im==v).sum() for v in range(256)])
    p = p/p.sum()
    # Compute e = -sum(p(g)*log2(p(g)))
    e = -(p[p>0]*np.log2(p[p>0])).sum()
    return e

entropy_original = entropy(myImage_array_original)
entropy_shrinked = entropy(myImage_array_sh)
entropy_stretched = entropy(myImage_array)
entropy_equilized = entropy(equ)
print(f'entropy of original image is {entropy_original}')
print(f'entropy of shrinked image is {entropy_shrinked}')
print(f'entropy of stretched image is {entropy_stretched}')
print(f'entropy of equilized image is {entropy_equilized}')

#he
shrinked = cv2.imread("Third/anime_shrink.jpg",0)
stretched = cv2.imread("Third/anime_stretch.jpg",0)
equilized = cv2.imread("Third/anime_equilized.jpg",0)
A = cv2.subtract(shrinked , stretched)
B = cv2.subtract(shrinked , equilized)
C = cv2.subtract(stretched , equilized)
plt.figure()
plt.subplot(1,3,1)
plt.imshow(A)
plt.title('A')
plt.subplot(1,3,2)
plt.imshow(B)
plt.title('B')
plt.subplot(1,3,3)
plt.imshow(C)
plt.title('C')


#ve
entropy_A = entropy(A)
entropy_B = entropy(B)
entropy_C = entropy(C)
print(f'entropy of A image is {entropy_A}')
print(f'entropy of B image is {entropy_B}')
print(f'entropy of C image is {entropy_C}')

plt.show()