from PIL import Image
import numpy as np
import math
import seaborn as sns
from matplotlib import pyplot as plt
def open_image(file_path,show=False)->Image:
    im= Image.open(file_path)
    #im.rotate()
    if show==True:
        im.show()
        
        
        sns.heatmap(np.array(im,dtype=np.uint8), cmap='coolwarm', xticklabels=False, yticklabels=False)
        plt.show()
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

def shirnk(image):
    image_data = np.array(image,dtype=np.uint8)
    if len(image_data.shape) !=2:
        raise ValueError("Not a gray scale image")
    height,width = image_data.shape
    print(f"height is {height} width is {width}")
    center_x = int(width/2)
    center_y = int(height/2)
    shrink_matrix = np.zeros([height,width],dtype=np.uint8)
    shrink_parameter=0.5
    for i in range(width):
        for j in range(height):
            x_new = int((i)*shrink_parameter)
            y_new = int((j)*shrink_parameter)
            try :
                
                shrink_matrix[x_new,y_new]=image_data[i,j]
                
            except:
                raise IndexError("out of bounds during transposition")
    shrink_image = Image.fromarray(shrink_matrix)
    shrink_image.show()
    ...
def enlarge(image):
    image_data = np.array(image,dtype=np.uint8)
    if len(image_data.shape) !=2:
        raise ValueError("Not a gray scale image")
    height,width = image_data.shape
    print(f"height is {height} width is {width}")
    center_x = int(width/2)
    center_y = int(height/2)
    enlarge_matrix= np.zeros([height*2,width*2],dtype=np.uint8)
    enlarge_multiplier=2
    for i in range(width):
        for j in range(height):
            x_new = int((i)*enlarge_multiplier)
            y_new = int((j)*enlarge_multiplier)
            try :
                
                enlarge_matrix[x_new,y_new]=image_data[i,j]
                
            except:
                raise IndexError("out of bounds during transposition")
    
    sns.heatmap(enlarge_matrix, cmap='coolwarm', xticklabels=False, yticklabels=False)
    plt.show()
    enlarge_image = Image.fromarray(enlarge_matrix)
    enlarge_image.show()

def main():
    image_file_path = "../../image_data/cameraman.tif"
    img = open_image(image_file_path,show=True)
    #rotated_image = img.rotate(30)
    #rotated_image.show()
    #rotate(img)
    enlarge(img)
if __name__ == "__main__":
    main()