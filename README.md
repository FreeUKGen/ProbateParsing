# Probate-Parsing
Probate Parsing as a GSoC Student for Free UK Genealogy. Refer to the [wiki](https://github.com/FreeUKGen/ProbateParsing/wiki).

Free UK Genealogy aims to launch a new project to expose genealogical information from wills and probate books. These books record the date and location of people's deaths, their occupations, and often the same information about the family members that executed the wills.

In previous projects, all this material was transcribed manually by volunteers, as the source documents were handwritten. The probate books are different, however, in that they are printed and thus are accessible to OCR. We should be able to use OCR text to seed a database by parsing the text for names, dates, occupations, and relationships. We should also be able to use OCR bounding box coordinates to associate regions of a scanned page with an entry for presentation to researchers or for correction by volunteers.

Tools for OCR and parsing of probate books to be loaded into the MyopicVicar search engine.

## Features
**[Bounding Box](../master/Bounding_Boxes)**  
In phase 1, the scanned images of probate books are refined using Image Processing methods. For example, one page in a probate book consists of many entries. The aim of this phase is to isolate each entry by cropping the original image entry-wise to get the best possible output owing to some OCR discrepancies.

**[Optical Character Recognition](../master/OCR)**  
In phase 2, the cropped images of the probate books are parsed under an Optical Character Recognition algorithm to generate the information in text.

**[Named Entity Recognition](../master/NER)**  
One of the most challenging parts of the project involves extracting meaningful information from the text generated in Phase 2. For the algorithm to extract particular fields like name, relationships and occupation, it must “learn” the semantics of each probate entry. Methods that tackle such problems form an integral part of Natural Language Processing.

## Setup Instructions
### Install Python  
  **a.** If you use any Unix-based systems - macOS or Linux, then python will be preinstalled with the distribution.  

  **b.** If you are using Windows, use these steps to install Python. Refer [here](https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/) if you get stuck. Download Python 3.5 or higher.

  **Note** -
  - Add Python to the Environment Variables
  On the System Properties / Advanced tab, click Environment Variables to open User Variables and System Variables  

  - Create a new System Variable named Variable name: PYTHON_HOME and Variable value: c:\Python35 (or whatever your installation path was)

### Install pip   
Pip is the Python Package Manager and Installer.  

**1. Linux/macOS** - Similarly, you can also use pip installation script.  
Download the script on your using wget or curl, then run the script with appropriate python version for which you need to install pip. Refer [here](https://pip.pypa.io/en/stable/installing/) if you get stuck  

`curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"`   

`python3 get-pip.py  # For specific python version which we require`

**2. Windows** - There are many methods for getting Pip installed, but my preferred method is the following. Refer [here](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation) if you get stuck.  

Download get-pip.py to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run `python3 get-pip.py`.  

If you followed the Python installation instructions above, then you've already got the pip install location (default = C:\Python35\Scripts) in your Windows' PATH ENVIRONMENT VARIABLE.

### Install virtual environment (virtualenv)
Instead of installing packages system-wide in these instructions we use virtualenv to create an isolated Python environment and then install packages into this environment. This procedure is more demanding but has the advantage of being independent from the rest of the system. We can use pip to install virtualenv. Use the command -
  `pip3 install virtualenv`  

Once virtualenv is installed you can activate it using the following steps. Refer [here](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html) if you get stuck.

Go to a directory where you want to create a virtualenv and type the following command - `virtualenv -p python3 <virtualenv_name>`  

Ensure you type *python3*.
Go to the directory where the virtualenv was created. Open the terminal in the folder and type
`source <virtualenv_name>/bin/activate.`  
Ensure that virtualenv is present as shown by `(venv)`.


### Some cautionary instructions
1. Make sure that all directory names are not separated by spaces. Multi-word directory names should be connected by a - or \_.  

2. If installation of pip3 does not work, then just use pip instead of pip3 at all places.

3. It is not recommended to use Windows due to no pre-packaged support and different file system functionality, so if possible, use Unix/Linux systems.  

4. The code is written using Python v3 and not Python v2.7 so if you encounter any error, then it is most likely because you are running it on Python2.7.


### Dependencies Installation
1. Pull the code from the Github using `git clone https://github.com/FreeUKGen/ProbateParsing.git`  

2. Activate the virtual environment using  
`source <virtualenv_name>/bin/activate.`

3. Install requirements using the command -  
`pip3 install -r requirements.txt`  

4. You also need to download the spacy model. Download and install it using `python3 -m spacy download en`. Should not take more a few minutes.

5. You can use the setup.sh file to perform all the above setup. Tested with a Ubuntu 16.04, Python 3.5.2 setup. Not recommended because of the very large downloads which may fail. Find the setup file [here](../master/setup.sh). Before running it give it the appropriate permissions by typing in the terminal -   
`chmod +x setup.sh`
