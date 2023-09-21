import numpy as np
from PIL import Image
def imread(image_location:str):
    im = Image.open(image_location)
    im.show()
    image_location = "../../image_data/AppleTree.png"
#imread(image_location)
def rgb_to_bandw(image_file):
    image_data = image_file.astype(dtype=np.uint32)
    grey_data=(image_data[:,:,0]+image_data[:,:,1] + image_data[:,:,2])/3
    grey_data=grey_data.astype(dtype=np.uint8)
    grey_data[grey_data >200]=255
    grey_data[grey_data <=200]=0
    return grey_data

