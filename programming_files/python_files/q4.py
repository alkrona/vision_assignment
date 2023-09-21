import numpy as np
from PIL import Image
import logging
from lecture_function import rgb_to_bandw
logging.basicConfig(level=logging.INFO,filename="informationq4.log")
def centroid_finder(file_path):
    img = Image.open(file_path)
    img_data = np.array(img,dtype=np.uint8)
    img_data = rgb_to_bandw(img_data)
    img_data_x = 
    #logging.info(f"shape of the image is {img_data.shape}")


def main():
    file_path = "../../image_data/WhiteEllipse12019.tif"
    centroid = centroid_finder(file_path)
class image:
    def __init__(self,file_path):
        self.file_path=file_path
if __name__ =="__main__":
    main()