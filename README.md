# Probate-Parsing
Probate Parsing as a GSoC Student for Free UK Genealogy

Free UK Genealogy aims to launch a new project to expose genealogical information from wills and probate books. These books record the date and location of people's deaths, their occupations, and often the same information about the family members that executed the wills.

In previous projects, all this material was transcribed manually by volunteers, as the source documents were handwritten. The probate books are different, however, in that they are printed and thus are accessible to OCR. We should be able to use OCR text to seed a database by parsing the text for names, dates, occupations, and relationships. We should also be able to use OCR bounding box coordinates to associate regions of a scanned page with an entry for presentation to researchers or for correction by volunteers.

Tools for OCR and parsing of probate books to be loaded into the MyopicVicar search engine.

## Files used
[crop_to_ocr.py](../blob/master/crop_to_ocr.py) - This python script takes the directry containing cropped entries for a given image and creates a text file that produces OCR text on all the cropped entries.

[crop.py](../blob/master/crop.py) - This file will crop all images in a directory to concentrate the text on the image.

[hocr_output.sh](../blob/master/hocr_output.sh) - This shell script will produce a hocr file for each image file in a folder.

[hocr_parsing.py](../blob/master/hocr_parsing.py) - This python script is used to convert hocr output to cropped images based on bounding boxes of each entry.

[hocr_to_crop.py](../blob/master/hocr_to_crop.py) - This python script is used to convert hocr output to cropped images based on bounding boxes of each entry for a folder containing many images.
