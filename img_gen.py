from PIL import Image
from prompt_toolkit import prompt
import numpy as np

def convert_base(dec, to_base):
    ret = []
    x = dec
    while x != 0:
        rest = int(x % to_base)
        x = int(x / to_base)
        ret.insert(0, rest)

    return ret

magic = ""
with open('myfile.txt', 'r') as f:
    magic = f.read()

for i in range(0, sys.maxsize):
    magic += str(random.randint(0,9))

colors_pp = 4
img_h = 1920
img_w = 1080

if False:
    magic = prompt("Magic number: ")
    colors_pp = int(prompt("Colors per pixel: "))
    img_h = int(prompt("Image height: "))
    img_w = int(prompt("Image width: "))


magic_parts = []
exp_lim = 18
i = 0
# Max int ~ 10^19; partition in to 10^18 blocks, of 18 digits
while True:
    low = exp_lim*i
    if(low >= len(magic)):
        break
    magic_parts.append(magic[low:low+exp_lim])
    i+=1

x_a = [int(m) for m in magic_parts]


def get_color(color):
    max_color = pow(256,3)
    x = (max_color / colors_pp) * (color)
    color_conv = convert_base(x, 256)

    if len(color_conv) > 3:
        color_conv = color_conv[-3:]

    while len(color_conv) < 3:
        color_conv.insert(0, 0)

    return tuple(v for v in color_conv)


def gen_pixels(x_a, colors_pp, img_h, img_w):

    pixels = []
    for i in range(0, len(x_a)):
        conv = convert_base(x_a[i], colors_pp)
        pixels += conv

    if(len(pixels) > img_w*img_h):
        print("Magic number is too large for these dimensions and colors per pixels")
        exit()

    pix_i = 0
    image = [[(255, 255, 255) for w in range(0, img_w)] for h in range(0, img_h)]

    # Smarter pixels distribution can be done here
    for i in range(0, img_h):
        for j in range(0, img_w):
            image[i][j] = get_color(pixels[pix_i])
            pix_i += 1
            if pix_i >= len(pixels):
                return image

    return image


pixels = gen_pixels(x_a, colors_pp, img_h, img_w)
array = np.array(pixels, dtype=np.uint8)

img = Image.fromarray(array)
img.show()
