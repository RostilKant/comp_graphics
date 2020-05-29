from PIL import Image
from pylab import *

img = array(Image.open('witcher1.jpg').convert('L'))
gray()

def negative(img):
    neg_img = 255 - img
    imshow(neg_img)
    show()
    
def clamping_img(img, start = 0, end = 255):
    clamp_img = (float(end - start) / 255) * img + start
    imshow(clamp_img)
    show()

def squared_pixels(img):
    squared_img = (255.0 * img / 255.0) ** 2
    imshow(squared_img)
    show()

negative(img)
clamping_img(img,100,200)
squared_pixels(img)


 
