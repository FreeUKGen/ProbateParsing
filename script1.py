from bs4 import BeautifulSoup
from PIL import Image
import os, string

folder_path = "1873 Probate/F2/"
dest_path = "Cropped_F2/"
hocr_path = "1873 Probate/hocr_F2/"
folders = os.listdir(folder_path)
for files in folders:
    test_image = files
    filename = test_image.split(".")[0]+"_"
    original = Image.open(folder_path+test_image)
    max_w, max_h = original.size
    print(">>>>>>>>>>>>>>>"+test_image)
    with open(hocr_path+test_image+'.hocr', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    soup = BeautifulSoup(data, 'lxml')
    names = soup.find_all('div',attrs={"class":"ocr_carea"})
    print(len(names))
    for name in names:
        for name in names:
            if(name.text.strip() == "" or name.text.strip().startswith("Image") or len(name.text)<15):
                names.remove(name)

    entries = []
    for name in names:
        first_word = name.text.strip().split(" ")
        print(first_word[0])
        if(first_word[0].isupper() or '{' in name or '}' in name or first_word[0].split(string.punctuation)[-1].isupper()):
            entries.append(name)

    if(len(entries)==0 or len(entries)==1):
        print(test_image+" is stupid")
        continue

    for entry in entries:
        print(entry.text)

    coords_initial = entries[0].attrs['title'].split(" ")
    x1_curr = 0
    y1_curr = int(coords_initial[2])
    x2_curr = max_w
    y2_curr = int(coords_initial[4])
    i=0
    first=0
    for i in range(1, len(entries)):
        coords = entries[i].attrs['title'].split(" ")
        x1_future = 0
        y1_future = int(coords[2])
        x2_future = max_w
        y2_future = int(coords[4])
        print(str(i)+" "+str(y2_curr)+" "+str(y1_future))
        if(y1_future-y2_curr>0):
            if(first == 0):
                #print(entries[i].text)
                cropped_example = original.crop((x1_curr, 0, x2_curr, (y1_curr-30)))
                cropped_example.save(dest_path+filename+"0.jpg")
                cropped_example = original.crop((x1_curr, (y1_curr-60), x2_curr, y1_curr+(y1_future-y2_curr+30)))
                cropped_example.save(dest_path+filename+str(i)+".jpg")
                first = 1
            else:
                #print(entries[i].text)
                cropped_example = original.crop((x1_curr, (y1_curr-60), x2_curr, y1_curr+(y1_future-y2_curr+30)))
                cropped_example.save(dest_path+filename+str(i)+".jpg")

        elif(i==len(entries)-1 or y1_future-y2_curr<=0):
            print("Last element: "+entries[i].text)
            cropped_example = original.crop((x1_curr, (y1_future-60), x2_curr, max_h))
            cropped_example.save(dest_path+filename+str(i)+".jpg")
        x1_curr = x1_future
        x2_curr = x2_future
        y1_curr = y1_future
        y2_curr = y2_future
        i=i+1

    cropped_example = original.crop((x1_curr, (y1_future-60), x2_curr, max_h))
    cropped_example.save(dest_path+filename+str(i)+".jpg")
    os.remove(folder_path+files)
