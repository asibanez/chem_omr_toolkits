import os
import sys

if len(sys.argv) != 3:
    print('Usage: filelist_to_txt_v0 [input directory] [output directory]')
    exit()

input_folder = sys.argv[1]
output_folder = sys.argv[2]

file_list = os.listdir(input_folder)

output_filename = 'filelist.txt'
output_filepath = os.path.join(output_folder, output_filename)
open_file = open(output_filepath, 'w+')
for item in file_list:
    open_file.write(item)
    open_file.write('\n')
open_file.close()
