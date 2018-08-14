# Phase Walkthrough

## Features used in Phase 1:
1. [crop.py](../master/crop.py) - If the image file contains characters from previous/next pages it may interfere with the OCR. This file will crop all images in a directory to concentrate the text on the image. This is a basic preprocessing step and is highly recommended that before any of the below scripts are run, the images are cropped to remove any stray characters.

2. [hocr_output.sh](../master/hocr_output.sh) - This shell script will produce a hocr file for each image file in a folder.

3. [hocr_parsing.py](../master/hocr_parsing.py) - This python script is used to convert hocr output to cropped images based on bounding boxes of each entry.

4. [hocr_to_crop.py](../master/hocr_to_crop.py) - This python script is used to convert hocr output to cropped images based on bounding boxes of each entry for a folder containing many images.

**Note**: Bash files will not run directly on the Windows Command Prompt/ PowerShell. You will have to run the file on Git Bash. Please refer here to learn more.

## Dependencies in Phase 1:
1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - `pip install beautifulsoup4`  
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree prevalent in HTML files. Since the hOCR output is in an XML/HTML format, the relevant data in the image can be extracted using BeautifulSoup.

2. [Pillow](http://www.pythonware.com/products/pil/) - `pip install pillow`  
Python Imaging Library (in newer versions known as Pillow) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

3. [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)  
A. To install tesseract on Mac, first ensure that you have Homebrew installed. To install Homebrew, refer to this link. Once Homebrew is installed, type in the given command - `brew install tesseract`  
B. To install tesseract on Linux, type in the following command,`sudo apt-get install tesseract-ocr`  
C. To install tesseract on Windows, please refer to the documentation [here](https://github.com/tesseract-ocr/tesseract/wiki#windows).  

4. [lxml](https://github.com/lxml/lxml) - `pip install lxml`  
XML/ HTML parser for Python. lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.

Using the pip install commands, we can install Pillow and BeautifulSoup. Ensure that the virtual-environment is activated by typing `source <virtualenv-name>/bin/activate`.

## Expected Output:
[crop.py](../master/crop.py) - This file will crop all images in a directory to concentrate the text on the image.The width and height of the image that needs to be obtained is taken for all images.  
	`python3 crop.py <source_directory> <destination_directory>`

![crop.py](https://i.imgur.com/l3i0pwg.png)

**Note**: The paths mentioned in the terminal is not absolute. Running the script is relative to where you save your folders and files.

[hocr_output.sh](../master/hocr_output.sh) - The directory should contain image files for which you want to produce hOCR files. The shell script will produce the hOCR files of all the images present in the directory. The directory path is given as an argument. To execute shell scripts, you need to give it appropriate permissions.  
	`chmod +x hocr_output.sh`  
	To execute the script now type,  
    `./hocr_output.sh <source_directory>`

![hocr_output.sh](https://i.imgur.com/vH3sG4K.png)

[hocr_parsing.py](../master/hocr_parsing.py) - The script will give the resulting cropped entries on a given image. The input consists of the source image, source image hocr and destination directory. It uses two algorithms, descriptions of which are given in the file. You need to choose which algorithm to use.  
	`python3 hocr_parsing.py <path_to_image> <path_to_hocr_file> <destination_path>`

![hocr_parsing.py](https://i.imgur.com/sO7ngSU.png)

[hocr_to_crop.py](../master/hocr_to_crop.py) - This is a batch script that is used to find the cropped entries using bounding boxes. The input to the script is the source directory containing the images that need to be cropped, the path containing all the hocr files for the same image files and the destination path which will store all the cropped images.  
    `python3 hocr_to_crop.py <source_directory> <path_to_hocr_files> <destination_path>`

![hocr_to_crop.py](https://i.imgur.com/lphWPko.png)

![output](https://i.imgur.com/1FphrZv.png)
