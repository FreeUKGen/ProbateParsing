# Phase Walkthrough

## Data Annotation - Creating the training dataset
To train a model, the algorithm must learn some examples to understand the semantics of the input text and what are the named entities. It tries to learn them as a pattern and gain better insights when more annotated data is presented to it for learning. For example in our use-case - consider the following text.

```
COURTENAY William Andrew. “Effects under £200.  8 July. Administration of the effects of William Andrew i- Courtenay late of 417 Mile-End-road Stepney in the County of ' Middlesex who died 9 June 1873 at 417 Mile-End-road was granted at the Principal Registry to Lydia Courtenay of :NUSIF 417 Mile-End-road Widow the Relict. He
```

The algorithm should be able to learn that anything starting with £ will be money. Text near the words County of will be a county name etc.

Tool used to annotate the data is called Dataturks. It has pre-built support for all data annotation needs like image labeling, NLP tagging, classification etc. It is used to annotate all your data, Text, Image, Video, or Speech. You can take a look at the probate_books dataset here.

![Dataturks 2](https://i.imgur.com/ELI7D8o.png)

![Dataturks 1](https://i.imgur.com/BDgzWE1.png)

![Dataturks 3](https://i.imgur.com/flYk13p.png)


## Features used in Phase 3:
**[dataturks_to_spacy.py](../NER/dataturks_to_spacy.py)** - Creates NER training data in SpaCy format from JSON downloaded from Dataturks.Once you download the JSON file from Dataturks, you can load it using the python script.  

**[train_ner.py](../NER/train_ner.py)** - This script trains the Named Entity Recognition model and returns the trained model on the probate wills annotated data. The model can be imported to test the remaining entries that are not annotated to extract the entities.  

**[test_ner.py](../NER/test_ner.py)** - This script tests the Named Entity Recognition model against the unannotated probate data. The model can be imported to test the remaining entries that are not annotated to extract the entities.  

## Dependencies in Phase 3:
1. [SpaCy](https://spacy.io/usage/models)
spaCy's models can be installed as Python packages. This means that they're a component of your application, just like any other module. spaCy v2.0 features new neural models for tagging, parsing and entity recognition.
Install spacy using the following command,  
	`pip install -U spacy`  
Then, download and install a language model so that the semantics for the English language are used while training.  
     `python3 -m spacy download en`

2. [Pandas](https://pandas.pydata.org/)
Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy package and its key data structure is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.  
For downloading pandas, you may need to download numpy and cython. For most cases if you run the command -  
`pip install pandas`.  
If you encounter an error then you can download it using the command -  
`pip install numpy python-dateutil pytz six numpy`.


3. [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
	openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.  
	`pip install openpyxl`


## Expected Output:
**[dataturks_to_spacy.py](../NER/dataturks_to_spacy.py)** - Once you download the dataturks annotated data from Dataturks, you need to convert it to a format that is acceptable for SpaCy while training. It accepts the json file and destination directory as input. It outputs the training data in a pickle file having a format which can be used for training using SpaCy.  
`python3 dataturks_to_spacy.py <path_to_json_file> <destination_path>`

![dataturks_to_spacy](https://i.imgur.com/mpjsCPR.png)

**[train_ner.py](../NER/train_ner.py)** - The input to the script is the pickle file generated during the dataturks_to_spacy.py and returns the trained model on the probate wills annotated data. The model can be imported to test the remaining entries that are not annotated to extract the entities.  
	`python3 train_ner.py <path_to_pickle_file> <model_destination_path>`

![train_ner](https://i.imgur.com/bnh3pUs.png)

**Note**: Make sure that you create a new folder for the trained model and add it to the destination path.

**[test_ner.py](../NER/test_ner.py)** - The input to the script is the folder containing the training model generated during the train_ner.py and a text file containing all the entries that need to be extracted. The output will be a excel, csv and tsv file.  
`python3 test_ner.py <path_to_model_directory> <path_to_test_data> <destination_path_for_files>`

![test_ner](https://i.imgur.com/mvJDrhO.png)

The excel, csv and tsv files are stored [here](https://github.com/FreeUKGen/ProbateParsing/tree/master/Inference_Data) for perusal.

![csv file](https://i.imgur.com/YQ6pIgr.png)
