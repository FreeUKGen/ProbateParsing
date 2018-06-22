'''
If the image file contains characters from previous/next pages it may interfere with the OCR. This file will crop all images in a directory to concentrate the text on the image.

The width and height of the image that needs to be obtained is taken for all images. A safe assumption is made for all images in a directory so that no text gets cropped.

python3 crop.py <source_directory> <destination_directory>
'''


from PIL import Image
import sys
import os

folder_path = sys.argv[1]
dest_path = sys.argv[2]
optimal_w = 2458
optimal_h = 3906

folders = os.listdir(folder_path)
for files in folders:
    file = files.split('/')[-1]
    print(file)
    original = Image.open(folder_path + file)
    width, height = original.size
    crop_w = width - optimal_w
    crop_h = height - optimal_h
    cropped = original.crop((int(crop_w / 2), int(crop_h / 2), int(width - (crop_w / 2)), int(height - (crop_h / 2))))
    cropped.save(dest_path + file)
