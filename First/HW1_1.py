from PIL import Image, ImageOps
import numpy as np

myImage = Image.open('First/foxy.png').convert('L')
# myImage.save('First/foxy_gry.png')
#1
resized_128 = myImage.resize((128, 128))
resized_128.save('First/foxy_128.png')
#4
resized_128_array = np.array(resized_128)

for i, lst in enumerate(resized_128_array):
    for j, item  in enumerate(lst):
        k = format(item,'08b')
        n = k[:4]
        m = int(n, 2)
        resized_128_array[i][j] = m
        
resized_128_array_4bit = resized_128_array*17
image_4bit = Image.fromarray(resized_128_array_4bit)
image_4bit.save('First/foxy_4bit.png')
#2
resized_32 = myImage.resize((32, 32))
resized_32.save('First/foxy_32.png')
#3
myImage_32 = Image.open('First/foxy_32.png').convert('L')
resized_32to512 = myImage_32.resize((512, 512))
resized_32to512.save('First/foxy_512_new.png')
#6
inverted_128 = ImageOps.invert(resized_128)
inverted_128.save('First/foxy_inv.png')