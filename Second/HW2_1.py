from PIL import Image, ImageOps
import numpy as np

my_image = Image.open('Second/me.jpg').convert('L')
my_image.save('Second/me_gray.jpg')
my_image_array_4 = np.array(my_image)
my_image_array_1 = np.array(my_image)
my_image_array_t = np.array(my_image)
my_image_array_s = np.array(my_image)

#1
for i, lst in enumerate(my_image_array_4):
    for j, item  in enumerate(lst):
        k = format(item,'08b')
        n = k[:4]
        m = int(n, 2)
        m = m * 17
        my_image_array_4[i][j] = m

image_4bit = Image.fromarray(my_image_array_4)
image_4bit.save('Second/me_4bit.jpg')

#2
for i, lst in enumerate(my_image_array_1):
    for j, item  in enumerate(lst):
        k = format(item,'08b')
        n = k[:1]
        m = int(n, 2)
        m = m * 255
        my_image_array_1[i][j] = m

image_1bit = Image.fromarray(my_image_array_1)
image_1bit.save('Second/me_1bit.jpg')

#3
text = 'I am Fatemeh Taher. Currently accepted in Kharazmi university.'
text_binary_two_bits = []
for character in text:
    character_integer = ord(character)
    character_binary = format(character_integer,'08b')
    for i,j in zip(character_binary[0::2],character_binary[1::2]):
        text_binary_two_bits.append(i+j)

for i, lst in enumerate(my_image_array_t):
    o = len(text_binary_two_bits)
    p = 0
    for j, item  in enumerate(lst):
        k = format(item,'08b')
        n = k[:6]
        n = n + text_binary_two_bits[p]
        p += 1
        m = int(n, 2)
        my_image_array_t[i][j] = m
        if p >= o:
            break
    if p >= o:
        break

image_with_text = Image.fromarray(my_image_array_t)
image_with_text.save('Second/me_with_text.jpg')

text_counter = 0
backward_text = ''
for i, lst in enumerate(my_image_array_t):
    o = len(text)*4
    char_counter = 0
    n = ''
    for j, item  in enumerate(lst):
        text_counter += 1
        if (text_counter>o):
            break
        k = format(item,'08b')
        n = n + k[6:]
        
        char_counter += 1
        if (char_counter==4):
            char_counter = 0
            m = int(n,2)
            char = chr(m)
            n = ''
            backward_text = backward_text + char
    if (text_counter>o):
            break

print(f'This is a hidden text: {backward_text}')

#4
quarter = my_image_array_s.shape[0]//2
print(my_image_array_s.shape)
for i, lst in enumerate(my_image_array_s[:quarter]):
    for j, item in enumerate(lst[:quarter]):
        k = format(item,'08b')
        n = '0' + k[:7]
        m = int(n, 2)
        m = 255*(m/255)**0.7
        my_image_array_s[i][j] = m

image_with_power = Image.fromarray(my_image_array_s)
image_with_power.save('Second/me_powerlaw.jpg')