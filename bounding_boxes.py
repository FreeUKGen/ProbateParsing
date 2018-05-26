import cv2 as cv
import os
import sys

folder_path = sys.argv[1]
dest_path = sys.argv[2]
X = []
y = []
folders = os.listdir(folder_path)
for files in folders:
    # print(folder)
    # if(os.listdir(folder_path + '/' + folder)):
    #     files = os.listdir(os.path.join(folder_path, folder))
    # for file in files:
    if(str(files).lower().endswith((".jpg", ".jpeg")) is True and not str(files).startswith('.')):
        image_path = folder_path + files
        print(image_path)
        filename = files.split('/')[-1]
        img = cv.imread(image_path, 0)
        print(img)
        img = cv.resize(img, (512, 512))
        edges = cv.Canny(img, 512, 512)
        print(edges)
        path = dest_path + '/' + str(files)
        print(path)
        cv.imwrite(path, edges)


# plt.subplot(121),plt.imshow(rsz_img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()
