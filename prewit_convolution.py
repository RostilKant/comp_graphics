from cv2 import cv2
from skimage import img_as_int,img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

witcher = cv2.imread('witcher1.jpg',0)
img = img_as_int(witcher)

prewit_vertical = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype='float64')

prewit_vertical_out = img_as_ubyte(ndimage.convolve(img,prewit_vertical,mode='constant',cval=0.0))
plt.imshow(prewit_vertical_out, cmap="gray")
plt.show()