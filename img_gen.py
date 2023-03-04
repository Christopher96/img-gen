from PIL import Image
from prompt_toolkit import prompt
import numpy as np

x = int(prompt("Magic number: "))
base = int(prompt("Colors per pixel: "))
img_h = int(prompt("Image height: "))
img_w = int(prompt("Image width: "))
img_name = "gen.png"

last_img = pow(base, img_h*img_w)
if(x > last_img):
    print("Magic number is too large for these dimensions")
    exit()

def gen_pixels(x, base, img_h, img_w):

    pixels = [[(255, 255, 255) for j in range(0, img_h)] for i in range(0, img_w)]

    for i in range(0, img_w):
        for j in range(0, img_h):
            if x == 0:
                return pixels
            else:
                rest = x%base
                x = int(x/base)
                pixels[i][j] = (255, rest, 255)

    return pixels


pixels = gen_pixels(x, base, img_h, img_w)
array = np.array(pixels, dtype=np.uint8)

img = Image.fromarray(array)
img.show()
