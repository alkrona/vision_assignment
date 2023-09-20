import numpy as np
from PIL import Image
def imread(image_location:str):
    im = Image.open(image_location)
    im.show()
image_location = "../../image_data/AppleTree.png"
#imread(image_location)
def rgb_to_grey(image_file:str):
    im = Image.open(image_location)
    image_data = np.array(im)
    grey_data=(image_data[:,:,0]+image_data[:,:,1] +image_data[:,:,2])/3
    print(grey_data.shape)
    gray_img = Image.fromarray(grey_data)
    gray_img = gray_img.convert('L')
    gray_img.show()

    
    print(image_data.shape)
rgb_to_grey(image_location)