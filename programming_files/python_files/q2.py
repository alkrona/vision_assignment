from PIL import Image
import numpy as np
import math
def open_image(file_path,show=False)->Image:
    im= Image.open(file_path)
    #im.rotate()
    if show==True:
        im.show()
    return im
def rotate(image):
    image_data = np.array(image,dtype=np.uint8)
    if len(image_data.shape) !=2:
        raise ValueError("Not a gray scale image")
    height,width = image_data.shape
    print(f"height is {height} width is {width}")
    center_x = int(width/2)
    center_y = int(height/2)
    cos_val = np.cos(math.radians(30))
    sin_val = np.sin(math.radians(30))
    rotated_matrix = np.zeros([height*2,width*2],dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            y_new = int(-(i-center_x)*sin_val + (j-center_y)*cos_val + center_y*2)
            x_new = int((i-center_x)*cos_val + (j-center_y)*sin_val + center_x*2)
            if 0<y_new<rotated_matrix.shape[0] and 0<x_new<rotated_matrix.shape[1]:
                try:
                    rotated_matrix[x_new,y_new]=image_data[i,j]
                except:
                    raise ValueError("index out of bound during transposintion")
    
    print(f"x center is {center_x} and y center is {center_y}")
    print(f"shape of rotated matrix is {rotated_matrix.shape}")
    print(rotated_matrix)
    rotated_image = Image.fromarray(rotated_matrix)
    rotated_image.show()
def main():
    image_file_path = "../../image_data/cameraman.tif"
    img = open_image(image_file_path,show=True)
    #rotated_image = img.rotate(30)
    #rotated_image.show()
    rotate(img)
if __name__ == "__main__":
    main()