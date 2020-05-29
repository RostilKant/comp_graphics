import scipy.misc
import scipy.ndimage
from PIL import Image

img = Image.open("lena_noisy.png")
result_img = scipy.ndimage.filters.median_filter(img,size = 5, footprint = None, 
output=None, mode = 'reflect',cval=0.0, origin = 0)
result_img = Image.fromarray(result_img)
img.show()
result_img.show()