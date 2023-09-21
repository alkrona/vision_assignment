import numpy as np
from PIL import Image
import logging
from lecture_function import rgb_to_bandw
from matplotlib import pyplot as plt
logging.basicConfig(level=logging.INFO,filename="information_q5.log")
import pandas as pd
import seaborn as sns
def main():
    file_name = "../../image_data/WhiteMix2019.tif"
    logging.info(f"took the file")
    pre_procesed_image= preprocessing(file_name)
    logging.info(f"preprocessed the image")
    #showing image 
    Image.fromarray(pre_procesed_image).show()
    blobdata,array=diferenciate_blobs(pre_procesed_image)
    logging.info(f"this is the useful array{array}")
    df = pd.DataFrame(blobdata)
    df.to_csv("txtq5.csv")
    postprocessing(blobdata)
def preprocessing(file_path:str)->np.array:
    return rgb_to_bandw(np.array(Image.open(file_path),dtype=np.uint8))
def postprocessing(labeled_array:np.array)->np.array:
    height, width = labeled_array.shape
    colored_array = np.zeros((height, width, 3), dtype=np.uint8)
    unique_labels = np.unique(labeled_array)
    unique_labels = unique_labels[unique_labels != 0]  # Exclude 0 if it represents the background
    palette = sns.color_palette("hsv", len(unique_labels))
    palette = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in palette]
    for i, label in enumerate(unique_labels):
        colored_array[labeled_array == label] = palette[i]

    
     # Blue color for blobs labeled with 3
    
    plt.imshow(colored_array)
    plt.show()

def diferenciate_blobs(blob_data:np.array)->np.array:
    height,width = blob_data.shape
    eq_list=[]
    eq_list.append(0)
    count=1
    logging.info(f" the eqlist at the start is {eq_list}")
    for i in range(1,width-1):
        for j in range(1,height-1):
            if blob_data[i,j]==0:
                pass
            if blob_data[i,j]==255:
                #case1 no surrounding non zero element
                if blob_data[i,j-1] ==0 and blob_data[i-1,j-1]==0 and blob_data[i-1,j]==0 and blob_data[i-1,j+1]==0:
                    blob_data[i,j]=count
                    eq_list.append(count)
                    count+=1
                #case2 one surrounding non-zero element
                temp_list = np.array([blob_data[i,j-1],blob_data[i-1,j-1],blob_data[i-1,j],blob_data[i-1,j+1]],dtype=np.uint8)
                if np.count_nonzero(temp_list)==1:
                    blob_data[i,j]=np.max(temp_list)
                    eq_list.append(np.max(temp_list))
                elif np.count_nonzero(temp_list)>1:
                    #case with multiple blobs surrounding
                    try:
                        minimum=np.min(temp_list[temp_list>0])
                    except :
                        logging.info(f" this array cause the problem {temp_list}")
                        raise ValueError
                    blob_data[i,j]=minimum

                    temp_list[temp_list>0]
                    for element in temp_list:
                        try:
                            pass
                            eq_list[element]=minimum
                        except IndexError:
                            logging.info(f" faliure occured at element {i,j}")
                            logging.info(f"this is the temp list {temp_list}")
                            df = pd.DataFrame(blob_data)
                            df.to_excel("output.xlsx")
                            logging.info(f" code failed when it tried to push {element} in {eq_list}")
                            raise IndexError
    return(blob_data,temp_list)            
                                                                                                    
    
if __name__ == "__main__":
    main()