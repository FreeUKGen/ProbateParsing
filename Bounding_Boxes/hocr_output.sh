for filename in "$1"*; do echo "tesseract ${filename} ${filename} hocr"; tesseract ${filename} ${filename} hocr; done
