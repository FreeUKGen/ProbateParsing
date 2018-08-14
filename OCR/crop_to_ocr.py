'''
This python script takes the directry containing cropped entries for a given image and creates a text file that produces OCR text on all the cropped entries.
Method 1 creates a separate file for each parent image from all the cropped entries.
Method 2 creates a file for all the entries in a directory
python3 crop_to_ocr.py <source_directory> <destination_directory>
Dependencies
1. pytesseract
    Install tesseract using sudo apt-get install tesseract-ocr
    Install pytesseract using pip install pytesseract
2. Pillow
    pip install Pillow
'''

import os
import sys
import pytesseract
from PIL import Image
import re


folder_path = sys.argv[1]
dest_path = sys.argv[2]
folder = os.listdir(folder_path)
checked = {}    # all files that have already been used for OCR

if dest_path is not None:
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

folder_path = folder_path + "/" if (folder_path[-1] is not '/') else folder_path
dest_path = dest_path + "/" if (dest_path[-1] is not '/') else dest_path


def stringSplitByNumbers(x):
    r = re.compile('_')
    l = r.split(x)
    return [int(y) if y.isdigit() else y for y in l]


folder = [file.replace('.jpg', '') for file in folder]
folder = sorted(folder, key=stringSplitByNumbers)
folder = [file + '.jpg' for file in folder]

print("Enter your choice for OCR method\n1. One file for each image\n2. One file for each directory\n")

ch = int(input())

for file in folder:
    checked[file] = 0  # initializing all files

if(ch == 1):
    for file in folder:
        print(file)
        file_base = file.split('_')

        if int(file_base[1].split('.')[0]) == 0:    # if there is a continuation of text to the next page
            name = ""
            number = str(int(file_base[0]) - 1)     # fetching previous file name
            for i in range(0, (5 - len(number))):
                name = "0" + number
                number = name
            f = open(dest_path + name + ".txt", "a+")
            checked[file] = 1
            text = pytesseract.image_to_string(Image.open(folder_path + file))  # OCR on image
            f.write(text)
            f.close()

        if checked[file] == 0:
            f = open(dest_path + file_base[0] + ".txt", "a+")    # open file
            text = pytesseract.image_to_string(Image.open(folder_path + file))  # OCR on image
            f.write("\n##########\n")
            f.write(text)   # write text to file
            checked[file] = 1
            for i in folder:
                if os.path.isfile(os.path.join(folder_path + i)) and file_base[0] in i and checked[file] == 0:
                    checked[i] = 1
                    text = pytesseract.image_to_string(Image.open(folder_path + i))
                    f.write("\n##########\n")
                    f.write(text)
            f.close()   # close file

        else:
            continue


elif(ch == 2):
    f = open(dest_path + folder_path.split('/')[-2] + ".txt", "a+")
    for file in folder:
        print(file)
        file_base = file.split('_')
        if checked[file] == 0:
            if int(file_base[1].split('.')[0]) == 0:
                text = pytesseract.image_to_string(Image.open(folder_path + file))  # OCR on image
                f.write(text)   # write text to file
                checked[file] = 1
            else:
                text = pytesseract.image_to_string(Image.open(folder_path + file))  # OCR on image
                f.write("\n##########\n")
                f.write(text)   # write text to file
                checked[file] = 1

        else:
            continue

    f.close()   # close file


# clean the data
for file in sorted(os.listdir(dest_path)):
    if(os.path.isdir(dest_path + file)):
        continue
    else:
        with open(dest_path + file, 'r') as myfile:
            file_data = myfile.read().replace('\n', ' ')
        data = file_data.split("##########")
        data.remove(data[0])
        file_write = open(dest_path + "cleaned_" + file, "w")
        for entry in data:
            file_write.write("%s\n" % entry)
        os.remove(dest_path + file)   # comment this if you want the raw ocr files
