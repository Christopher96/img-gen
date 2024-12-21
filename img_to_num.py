import math
import numpy as np

from PIL import Image

class Fraction:
    def __init__(self, num):
        self.nominator = num
        self.denominator = int(''.join(['9' for i in range(0, len(str(num)))]))

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

class ImgToBlocks:

    def add_color(self, color):
        # We can convert from any base to decimal with 1234_x = 1*x^3 + 2*x^2 + 3*x^1 + 4*x^0
        # Iterate (block_size-1)-0 for each number, when idx reaches 0 start new block

        if(self.idx == 0):
            # x^0 = 1
            # print(self.idx, self.current_block_val, int(color))
            self.current_block_val = int(self.current_block_val) + int(color)
            # print()
            # print(self.current_block_val)
            # print()

            # Add block value and reset
            self.blocks.append(self.current_block_val)
            self.asd += 1
            self.idx = block_size-1
            self.current_block_val = 0
        else:
            # print(self.idx, self.current_block_val, int(color*int(math.pow(256, self.idx))))
            self.current_block_val = int(self.current_block_val) + int(color*int(math.pow(256, self.idx)))
            self.idx -= 1


    def __init__(self, img, block_size):
        pix = img.load()
        x_len, y_len = img.size

        self.idx = block_size-1
        self.current_block_val = 0

        self.blocks = []

        self.asd = 0

        for y in range(0, y_len):
            for x in range(0, x_len):
                pixel = pix[x,y]
                # print(pixel)
                for color in pixel:
                    # print(color, end=',')
                    self.add_color(color)
                    # if self.asd > 5:
                    #     return

        # Add last block value even if it doesn't fill up the block
        if(self.idx > 0):
            self.blocks.append(self.current_block_val)

        # for block in blocks:
        #     frac = Fraction(block)
        #     print(frac)


class BlocksToImg:

    def convert_base(self, dec, to_base, block_size):
        ret = []
        x = dec
        # print('{:d}'.format(x))
        
        for i in range(0, block_size):
            rest = int(x % to_base)
            x = int(x / to_base)
            ret.insert(0, rest)

        return ret

    def __init__(self, img_size, blocks, block_size):        
        x_len, y_len = img_size

        colors = []

        asd = 0
        for block_num in blocks: 
            block_colors = self.convert_base(block_num, 256, block_size)
            for color in block_colors:
                colors.append(color)
                print(color, end=',')
            # if asd == 5:
            #     break
            asd += 1
            print()
            print(block_num)

        pixels = [[(255, 255, 255) for x in range(0, x_len)] for y in range(0, y_len)]

        for y in range(0, y_len):
            for x in range(0, x_len):
                pixel = tuple(v for v in colors[:3])
                # print(pixel)
                colors = colors[3:]
                pixels[y][x] = pixel

        # array = np.array(pixels, dtype=np.uint8)
        # img = Image.fromarray(array)
        # img.save("output.jpg")


# Max int is 2^63 - 1 on a 64 bit processor
# In terms of base 255 this is:
# 255^x = (2^63 - 1) =>
# x = 63ln(2)/ln(255) = 7.88056... ~ 7
# We can fit 255^7 in an int

block_size = 7
img = Image.open('input2.jpg')

img_to_num = ImgToBlocks(img, block_size)
# print()
blocks_to_img = BlocksToImg(img.size, img_to_num.blocks, block_size)

