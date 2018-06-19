for filename in *; do echo "tesseract ${filename} ${filename} -psm 1 hocr"; tesseract ${filename} ${filename} -psm 1 hocr; done
