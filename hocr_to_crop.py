from bs4 import BeautifulSoup
from PIL import Image
test_image = "00003.jpg"
original = Image.open(test_image)

with open('00003.hocr', 'r') as myfile:
    data=myfile.read().replace('\n', '')
print(data)
soup = BeautifulSoup(data, 'lxml')
names = soup.find_all('div',attrs={"class":"ocr_carea"})
print(len(names))
coords = names[2].attrs['title'].split(" ")
print(coords)

thresh = 50
i=0
for name in names:
    coords = name.attrs['title'].split(" ")
    print(coords)
    x_initial = 0
    y_initial = int(coords[2])
    x_final = 2774
    y_final = int(coords[4])
    if(y_final-y_initial>=150 and y_final-y_initial!=4297):
        cropped_example = original.crop((x_initial, y_initial, x_final, y_final+thresh))
        cropped_example.save("output1"+str(i)+".jpg")
        i=i+1
