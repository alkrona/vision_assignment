import numpy as np
from PIL import Image
def imread(image_location:str):
    im = Image.open(image_location)
    im.show()
image_location = "assignment3/image_data/AppleTree.png"
imread(image_location)
