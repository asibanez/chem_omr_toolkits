# chooses files from directories based on list in text file
# v0 base
# v1 changes filenames to consecutive IDs

import os
import sys
import shutil

if len(sys.argv) != 2:
    print('Usage: pick_image_v0.py [destination_folder]')
    exit()

destination_folder = sys.argv[1]
current_folder = os.getcwd()

open_src = open('sty-src-test.txt', 'r')

for counter, item in enumerate(open_src.readlines()):
    filepath = item.replace('\n', '')
    filename = str(counter) + '.png'
    origin_path = os.path.join(current_folder, filepath)
    destination_path = os.path.join(destination_folder, filename)
    shutil.copyfile(origin_path, destination_path)

open_src.close()