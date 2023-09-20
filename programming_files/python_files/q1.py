import numpy  as np
from PIL import Image
from matplotlib import pyplot as plt
def green_extraction(image_path):
    ...
def red_apple_detection(image_path:str)->list:
    rgb_image = Image.open(image_path)
    rgb_data = np.array(rgb_image,dtype=np.uint32)
    green_image_data = rgb_data[:,:,1]
    red_image_data = rgb_data[:,:,0]
    #print(green_image_data)
    gray_image_data = (rgb_data[:,:,0] + rgb_data[:,:,1]+rgb_data[:,:,2] )/3
    """ print(gray_image_data)
    fig = plt.figure(figsize =(10, 7))
    plt.hist(gray_image_data,bins=[0,50,100,150,200,250,300])
    #difference_image_data = gr
    plt.title("Numpy Histogram")
 
    # show plot
    plt.show()"""
    gray_image_data[gray_image_data>200]=0 # setting white spaces to dark
    red_image_data[gray_image_data==0]=0 # using the previous modified gray image as a mask to set white spaces in red image to dark
    red_image_data=red_image_data-gray_image_data  # eleminating non red elements 
    red_image_max = np.max(red_image_data) # finding max red values in red matrix
    red_image_data[red_image_data<0.8*red_image_max]=0 # eliminating elements that are far from max red value
    list_of_red_apples = np.nonzero(red_image_data) # finding array locations of non-zero elements
    return(list_of_red_apples)
def main():
    image_file_path=  "../../image_data/AppleTree.png"
    print(red_apple_detection(image_file_path))
if __name__ == "__main__":
    main()