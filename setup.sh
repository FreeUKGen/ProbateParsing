#!/bin/bash
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3 get-pip.py
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate.
git clone https://github.com/FreeUKGen/ProbateParsing
cd ProbateParsing
pip3 install -r requirements.txt
python3 -m spacy download en
