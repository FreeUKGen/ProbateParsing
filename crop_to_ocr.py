'''
This python script takes the directry containing cropped entries for a given image and creates a text file that produces OCR text on all the cropped entries.

Method 1 creates a separate file for each parent image from all the cropped entries.

Method 2 creates a file for all the entries in a directory

python3 crop_to_ocr.py <source_directory> <destination_directory>

Dependencies
1. pytesseract
    Install tesseract using sudo apt-get install tesseract-ocr
    Install pytesseract using pip3 install pytesseract

2. Pillow
    pip3 install Pillow
'''

import os
import sys
import pytesseract
from PIL import Image

folder_path = sys.argv[1]
dest_path = sys.argv[2]
folder = os.listdir(folder_path)
checked = {}    # all files that have already been used for OCR

print("Enter your choice for OCR method\n1. One file for each image\n2. One file for each directory\n")

ch = int(input())

for file in sorted(folder):
    checked[file] = 0  # initializing all files

if(ch == 1):
    for file in sorted(folder):
        file_base = file.split('_')
        print(file)
        if checked[file] == 0:
            f = open(dest_path + "/" + file_base[0] + ".txt", "a+")    # open file
            text = pytesseract.image_to_string(Image.open(folder_path + "/" + file))  # OCR on image
            f.write(text)   # write text to file
            f.write("\n--------------------\n")
            checked[file] = 1
            for i in sorted(folder):
                if os.path.isfile(os.path.join(folder_path + "/" + i)) and file_base[0] in i and checked[file] == 0:
                    checked[i] = 1
                    text = pytesseract.image_to_string(Image.open(folder_path + "/" + i))
                    f.write(text)
                    f.write("\n--------------------\n")
            f.close()   # close file

        else:
            continue

elif(ch == 2):
    f = open(dest_path + "/" + folder_path.split('/')[-2] + ".txt", "a+")
    for file in sorted(folder):
        print(file)
        if checked[file] == 0:
            text = pytesseract.image_to_string(Image.open(folder_path + "/" + file))  # OCR on image
            f.write(text)   # write text to file
            f.write("\n--------------------\n")
            checked[file] = 1

        else:
            continue

    f.close()   # close file
