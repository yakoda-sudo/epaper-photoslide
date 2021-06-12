##
 #  @filename   :   main.cpp
 #  @brief      :   5.65 inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 28 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

from waveshare_epd import epd5in65f
from PIL import Image
from PIL import *
import time
import os
import random
#the resolution of 5.65 epaper display
EPD_WIDTH = 600
EPD_HEIGHT = 448

#define palette array
palettedata = [
        0, 0, 0,
        255, 255, 255,
        67, 138, 28,
		100, 64, 255,
        191, 0, 0,
		255, 243, 56,
		232, 126, 0,
		194 ,164 , 244
    ]
p_img = Image.new('P', (16, 16))
p_img.putpalette(palettedata * 32)

def choose_random_loading_image(path):
    images=os.listdir(path)
    loading_image=random.randint(0,len(images)-1)
    return path+images[loading_image]

def main():
    epd = epd5in65f.EPD()
    epd.init()
    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    ImageDraw.Draw(image)
    image = Image.open(choose_random_loading_image('jpg/'))
#    logging.info("1.Drawing on the image...")
    print('the loaded pic is:', image)
#   resize the source image to target resolution
    resized_img = image.resize((EPD_WIDTH, EPD_HEIGHT))
#   replace the color to use 7 color palette
    colored_img = resized_img.quantize(palette=p_img)
    epd.display(epd.getbuffer(colored_img))
    time.sleep(7200)  # change the image every 2 hour
    main()


if __name__ == '__main__':
    main()
