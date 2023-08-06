##modified July14 2023 by yangqi 
##v1.8
##5.65inch module

from waveshare_epd import epd5in65f
from PIL import Image, ImageEnhance
from PIL import ImageDraw
import time
import os
import random
#the resolution of 5.65 inch epaper display
EPD_WIDTH = 600
EPD_HEIGHT = 448
display_dither = Image.FLOYDSTEINBERG

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
#    print('the loaded pic is:', image)
#   rotate the vertical image
    h, w = image.size
    if h < w:
        image = image.rotate(270, expand=True)
    else:
        pass
#   resize the source image to target resolution
    resized_img = image.resize((EPD_WIDTH, EPD_HEIGHT))
#   enhance the saturation of the image
    enhancer = ImageEnhance.Color(resized_img)
    saturation_level = 2.0
    colored_img = enhancer.enhance(saturation_level) 
    # Create a palette object
    pal_image = Image.new("P", (1,1))
    pal_image.putpalette((0,0,0, 255,255,255, 0,255,0, 0,0,255, 255,0,0, 255,255,0, 255,128,0) + (0,0,0)*249)

    # The color quantization and dithering algorithms are performed, and the results are converted to RGB mode
    colored_img = colored_img.quantize(dither=display_dither, palette=pal_image).convert('RGB')

    epd.display(epd.getbuffer(colored_img))
    time.sleep(7200)  # change the image every 2 hour
    main()

if __name__ == '__main__':
    main()
