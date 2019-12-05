"""Gets the names of correct images from the full list of image names and the list of correct image IDs"""

import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python select_correct_images_v0.py [image list path], [correct image id list path], [output directory]')
        exit()

    image_list_path = sys.argv[1]
    correct_image_id_list_path = sys.argv[2]
    output_path = os.path.join(sys.argv[3], 'correct_image_names.txt')    

    image_name_list_file = open(image_list_path)
    correct_image_id_list_file = open(correct_image_id_list_path)
    
    image_names = []
    correct_image_ids = []
    correct_image_names = []
    
    for item in image_name_list_file.readlines():
        image_names.append(item.replace('\n',''))
        
    for item in correct_image_id_list_file.readlines():
        correct_image_ids.append(item.replace('\n',''))

    correct_image_ids = [int(x) for x in correct_image_ids]
    correct_image_names = [image_names[i] for i in correct_image_ids] 
    
    with open(output_path, "w+") as open_file:
        for item in correct_image_names:
            open_file.write(str(item))
            open_file.write('\n')