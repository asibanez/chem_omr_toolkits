# automatically crops the images in the source directory and saves them to the target directory

from PIL import Image
import numpy as np
import tqdm
import sys
import os

def crop_image(image):

    image.load()       
    image_data = np.asarray(image)
    image_data_bw = image_data.max(axis=2)
    image_data_bw[image_data_bw == 255] = 0
         
    non_empty_columns = np.where(image_data_bw.max(axis = 0) > 0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis = 1) > 0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
    image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]
    cropped_image = Image.fromarray(image_data_new)
    return(cropped_image)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python image_crop_v0.py [source foloder], [destination folder]')
        exit()

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

image_list = os.listdir(source_folder)
image_list = [x for x in image_list if '.png' in x]

for file in tqdm.tqdm(image_list):
    image = Image.open(os.path.join(source_folder,file))
    cropped_image = crop_image(image)
    cropped_image.save(os.path.join(destination_folder,file))
