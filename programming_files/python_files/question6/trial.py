import logging
import numpy as np



logging.basicConfig(level=logging.INFO,filename="info.log")
eq_list= [0,1,1,2,4]
def find_parent(array,element):
    if array[element]==element:
        return element
    else :
        return find_parent(array,array[element])
print(find_parent(eq_list,3))
for index,ele in enumerate(eq_list):
    parent = find_parent(eq_list,index)
    logging.info(f"parent of index{index} is {parent}")
    eq_list[index]=parent
print(eq_list)