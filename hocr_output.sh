for filename in *; do echo "tesseract ${filename} ${filename} hocr"; tesseract ${filename} ${filename} hocr; done
