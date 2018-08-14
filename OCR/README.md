# Phase Walkthrough

## Features used in Phase 2:
**[crop_to_ocr.py](../OCR/crop_to_ocr.py)** - This python script takes the directory containing cropped entries for a given image and creates a text file that produces OCR text on all the cropped entries.

## Dependencies in Phase 2:
**1. [pytesseract](https://pypi.org/project/pytesseract/)** - `pip install pytesseract`  
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.  
Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Python Imaging Library, including jpeg, png, gif, bmp, tiff, and others, whereas tesseract-ocr by default only supports tiff and bmp. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file. Use the command.

**Note**: To use pytesseract, please ensure that you have Tesseract-OCR installed.

## Expected Output:

**[crop_to_ocr.py](../OCR/crop_to_ocr.py)** - The script takes the source directory containing all the cropped entries as and the destination directory for the text files as input. The script handles cleaning the OCR as well and produces two kinds of outputs. Method 1 creates a separate file for each parent image from all the cropped entries. Method 2 creates a file for all the entries in a directory. The method is asked at input.  
`python3 crop_to_ocr.py <source_directory> <destination_directory>`

![crop_to_ocr.py](https://i.imgur.com/2h0Jtkn.png)

Filewise OCR

![filewise](https://i.imgur.com/DX1fhYx.png)

Directory-wise OCR

![directorywise](https://i.imgur.com/GH4DLT4.png)
