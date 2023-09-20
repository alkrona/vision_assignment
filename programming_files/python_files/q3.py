from PIL import Image
import numpy as np
import pandas as pd
from q2 import open_image
import seaborn as sns
from matplotlib import pyplot as plt
#from lecture_function import rgb_to_grey
def image_file_list(image_path_list):
    image_array=[]
    for image_file in image_path_list:
        image_array.append(Image.open(image_file))
    return image_array
def corner_finder(image_list):
    square = np.array(image_list[2],dtype=np.uint32)
    square = (square[:,:,0]+ square[:,:,1]+square[:,:,2])/3
    square[square <200]=0
    square[square >200]=255
    square.astype(dtype=np.uint8)
    square_image = Image.fromarray(square)
    #square_image.show()
    height,width = square.shape
    Isobelx = np.zeros([height,width],dtype=np.double)
    Isobely = np.zeros([height,width],dtype=np.double)
    for i in range(2,width-1):
        for j in range(2,height-1):
            Isobelx[i,j]= abs(-1*square[i-1,j-1] + square[i-1,j+1]+ -2*square[i,j-1] + 2*square[i,j+1] -square[i+1,j-1] + square[i+1,j+1])
            
    #Isobelx.astype(np.uint8)
    #Iso_image_x = Image.fromarray(Isobelx)
   #Iso_image_x.show()
    for i in range(2,width-1):
        for j in range(2,height-1):
            Isobely[i,j]= abs(1*square[i-1,j-1] + 2*square[i-1,j]+ square[i-1,j+1] -1*square[i+1,j-1] -2*square[i+1,j] - square[i+1,j+1])
            
    #Isobely.astype(np.uint8)
    #Iso_image_y = Image.fromarray(Isobely)
    #Iso_image_y.show()
    df1 = pd.DataFrame(Isobelx)
    df1.to_csv("datax.csv")
    df2 = pd.DataFrame(Isobely)
    df2.to_csv("datay.csv")
    corner_data = np.sqrt(np.square(Isobelx)+ np.square(Isobely))
    corner_data.astype(dtype=np.uint8)
    Image.fromarray(corner_data).show()
    max_val = np.max(corner_data)
    corner_data.astype(dtype=np.double)
    #data_view = np.matrix(corner_data).view()
    #print(corner_data)
    df = pd.DataFrame(corner_data)
    df.to_csv("data1.csv")
    sns.heatmap(Isobelx, cmap='coolwarm', xticklabels=False, yticklabels=False)
    sns.heatmap(Isobely, cmap='coolwarm', xticklabels=False, yticklabels=False)
    sns.heatmap(corner_data, cmap='coolwarm', xticklabels=False, yticklabels=False)
    plt.show()
    ...
def main():
    image1_path="../../image_data/WhiteSquare2019.tif"
    #Image.open(image1_path).show()
    image2_path="../../image_data/WhiteRectangle2019.tif"
    #Image.open(image2_path).show()
    image3_path="../../image_data/WhiteTriangle2019.tif"
    #Image.open(image3_path).show()
    image4_path="../../image_data/WhiteDiamond2019.tif"
    #Image.open(image4_path).show()
    list1 = [image1_path,image2_path,image3_path,image4_path]
    list2 = image_file_list(list1)
    corner_finder(list2)
if __name__=="__main__":
    main()