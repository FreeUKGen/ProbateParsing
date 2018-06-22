import os
import pytesseract
from PIL import Image

folder_path = "1873 Probate/Cropped/Sample/"
dest_path = "1873 Probate/OCR/"
folders = os.listdir(folder_path)
checked = {}

for folder in sorted(folders):
    print(folder)
    for files in sorted(os.listdir(folder_path+folder)):
        checked[files]=0

    for files in sorted(os.listdir(folder_path+folder)):
        file_base = files.split('_')
        # do this at the end - checked[files] = 1
        print(files)
        if checked[files]==0:
            f = open(dest_path+folder+"/"+file_base[0]+".txt", "a+")
            text = pytesseract.image_to_string(Image.open(folder_path+folder+"/"+files))
            f.write(text)
            f.write("\n--------------------\n")
            checked[files] = 1
            for i in sorted(os.listdir(folder_path+folder)):
                if os.path.isfile(os.path.join(folder_path+folder+"/", i)) and file_base[0] in i:
                    print(">" + i)
                    checked[i] = 1
                    text = pytesseract.image_to_string(Image.open(folder_path+folder+"/"+i))
                    f.write(text)
                    f.write("\n--------------------\n")
            f.close()

        else:
            continue

