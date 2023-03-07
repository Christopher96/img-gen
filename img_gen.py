from PIL import Image
from prompt_toolkit import prompt
import numpy as np


x_a = []
colors = 3
img_h = 100
img_w = 100

if False:
    magic = prompt("Magic number: ")
    magic_parts = []

    exp_lim = 18
    i = 0
    # Number is to large to store
    while True:
        low = exp_lim*i
        if(low >= len(magic)):
            break
        magic_parts.append(magic[low:low+exp_lim])
        i+=1

    x_a = [int(m) for m in magic_parts]

    colors = int(prompt("Colors per pixel: "))
    img_h = int(prompt("Image height: "))
    img_w = int(prompt("Image width: "))


def get_color(color):
    max_color = pow(255,3)
    multiple = max_color / colors
    x = multiple * color
    color_conv = [0,0,0]
    i = 0
    while x != 0:
        rest = int(x % 255)
        x = int(x / 255)
        print(x)
        color_conv[i] = rest
        i += 1
        if(i >= 3):
            break

    return tuple(v for v in color_conv)

col = get_color(3)
print(col)
exit()

# last_img = pow(colors, img_h*img_w)
# if(x > last_img):
#     print("Magic number is too large for these dimensions")
#     exit()

def gen_pixels(x_a, colors, img_h, img_w):
    print(x_a)
    x_i = 0
    x = x_a[x_i]

    pixels = [[(255, 255, 255) for j in range(0, img_h)] for i in range(0, img_w)]

    for i in range(0, img_w):
        for j in range(0, img_h):
            if x == 0:
                if(x_i + 1 >= len(x_a)-1):
                    return pixels
                else:
                    x_i += 1
                    print(x_i)
                    x = x_a[x_i]
            else:
                rest = int(x % colors)
                x = int(x / colors)
                pixels[i][j] = (rest, rest, rest)

    return pixels


pixels = gen_pixels(x_a, colors, img_h, img_w)
print(pixels)
array = np.array(pixels, dtype=np.uint8)

img = Image.fromarray(array)
img.show()
