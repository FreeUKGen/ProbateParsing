'''
This python script is used to convert hocr output to cropped images based on bounding boxes of each entry.

To run the script:

python3 hocr_parsing.py <source_path> <destination_path> <path_to_hocr_file> <image_file>

Dependencies:
1. BeautifulSoup - pip3 install beautifulsoup4
2. Pillow - pip3 install Pillow

This method gets values of all bounding boxes in the hocr output - filters those entries which either have no value or those that do not start with uppercase or numeric values.

For example consider one entry

ABBOTT John Hesman.
Effects under £5,000.

Algorithm 1 filters entries with bounding boxes containing the above text i.e. the first word in the text should be uppercase (ABBOTT).

22 July. The Will of John Hesman Abbott late at
Royston in the County of Hertford Upholsterer who died
29 April 1873 at Royston was proved at the Principal
Registry by Louisa Abbott of Royston Widow the Relict
William John Abbott of Royston Upholster'er the Son and
Thomas Luke Gimson of Royston in the County of Cambridge

Algorithm 2 filters entries with bounding boxes containing the above text i.e. the first word in the text should be numeric (22).

'''
from bs4 import BeautifulSoup
from PIL import Image
import string
import sys

path = sys.argv[1]
dest_path = sys.argv[2]
hocr_path = sys.argv[3]
test_image = sys.argv[4]

filename = test_image.split(".")[0] + "_"
original = Image.open(path + test_image)
max_w, max_h = original.size

print("\nEnter your choice for algorithm\n\t1.Using LHS column bounding boxes\n\t2.Using RHS bounding boxes\nYour choice: ")
choice = input()

with open(hocr_path + test_image + '.hocr', 'r') as myfile:
    data = myfile.read().replace('\n', '')
soup = BeautifulSoup(data, 'lxml')

names = soup.find_all('div', attrs={"class": "ocr_carea"})

# removing ocr_carea elements that have no text or start with "Image" for "Image by FREEWILL"

for name in names:
    for name in names:
        if(name.text.strip() == "" or name.text.strip().startswith("Image") or len(name.text) < 15):
            names.remove(name)

entries = []
# Algorithm 1
if(int(choice) == 1):
    for name in names:
        first_word = name.text.strip().split(" ")
        if(first_word[0].isupper()):
            entries.append(name)    # list for all entries

# Algorithm 2
elif(int(choice) == 2):
    for name in names:
        first_word = name.text.strip().split(" ")
        if(first_word[0].isnumeric()):
            entries.append(name)    # list for all entries

coords_initial = entries[0].attrs['title'].split(" ")  # coordinates for first entry in the list
x1_curr = 0
y1_curr = int(coords_initial[2])
x2_curr = max_w
y2_curr = int(coords_initial[4])
i = 0
first = 0
for i in range(1, len(entries)):
    coords = entries[i].attrs['title'].split(" ")  # coordinates for next entry in the list
    x1_future = 0
    y1_future = int(coords[2])
    x2_future = max_w
    y2_future = int(coords[4])
    if(y1_future - y2_curr > 0):
        if(first == 0):  # if text of an entry spills over to the next page
            cropped_example = original.crop((x1_curr, 0, x2_curr, (y1_curr - 30)))
            cropped_example.save(dest_path + filename + "0.jpg")
            print(dest_path + filename + "0.jpg")
            cropped_example = original.crop((x1_curr, (y1_curr - 60), x2_curr, y1_curr + (y1_future - y2_curr + 30)))
            cropped_example.save(dest_path + filename + str(i) + ".jpg")
            print(dest_path + filename + str(i) + ".jpg")
            first = 1
        else:
            cropped_example = original.crop((x1_curr, (y1_curr - 60), x2_curr, y1_curr + (y1_future - y2_curr + 30)))
            cropped_example.save(dest_path + filename + str(i) + ".jpg")
            print(dest_path + filename + str(i) + ".jpg")

    elif(i == len(entries) - 1 or y1_future - y2_curr <= 0):
        cropped_example = original.crop((x1_curr, (y1_future - 60), x2_curr, max_h))
        cropped_example.save(dest_path + filename + str(i) + ".jpg")
        print(dest_path + filename + str(i) + ".jpg")

    x1_curr = x1_future
    x2_curr = x2_future
    y1_curr = y1_future
    y2_curr = y2_future
    i = i + 1

cropped_example = original.crop((x1_curr, (y1_future - 60), x2_curr, max_h))    # last entry
cropped_example.save(dest_path + filename + str(i) + ".jpg")
print(dest_path + filename + str(i) + ".jpg")
