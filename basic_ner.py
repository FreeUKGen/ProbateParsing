'''
This python script is used to produce named entities for each entry.

To run the script:

python3 basic_ner.py <source_path to OCR files for each image>

Dependencies:
1. SpaCy -
    To use SpaCy, you need to install the following
        a) pip3 install spacy
        b) sudo python3 -m spacy download en_core_web_lg
2. Pandas - pip3 install pandas

This method gets all named entities in the OCR output - filters those words in the text which either have no value.

For example consider one entry

ABBISS Jane Mary. _ Effects under £2,000.  15 November; Administratibn of the eﬂ‘ects of Jane Mary  "" Abhiss (Wife of James Abbiss) late of Ponders End in the County  of Middlesex who died 11 Febrnmy 1873 at Pondels End was  granted at the Principal Registry to the said James Abbiss of 61 Gracechurch- stxeet in the City of London Esquire.

The named entities generated are

[('ABBISS Jane Mary', 'PERSON'), ('2,000', 'MONEY'), ('15', 'CARDINAL'), ('November', 'DATE'), ('Administratibn', 'ORG'), ('Jane Mary', 'PERSON'), ('Abhiss (Wife of James Abbiss', 'WORK_OF_ART'), ('Middlesex', 'GPE'), ('11', 'CARDINAL'), ('1873', 'DATE'), ('Pondels End', 'ORG'), ('the Principal Registry', 'ORG'), ('James Abbiss', 'PERSON'), ('61', 'CARDINAL'), ('the City of London Esquire', 'GPE')]

These entities are then fed into the a Pandas dataframe that creates a tabular representation of the data and then produces a csv file of the named entities.

'''
import spacy
import sys
import os
import pandas as pd

data = []
file_name = []
directory_data = []
entities = []
ocr_data = ""

folder_path = sys.argv[1]

print("Enter your choice for NER method\n1. One csv file for each directory\n2. One csv file for all directories\n")

ch = int(input())

if(ch == 1):
    print("Enter folder name\n")        # enter directory name
    folder_name = input()
    for file in sorted(os.listdir(folder_path + folder_name)):
        with open(folder_path + folder_name + "/" + file, 'r') as myfile:
            file_data = myfile.read().replace('\n', ' ')
        file_name += (len(list(filter(None, file_data.split("##########")))) - 1) * [file]
        ocr_data = ocr_data + file_data + " "   # collecting data from ocr files
else:
    for folder in sorted(os.listdir(folder_path)):  # all directories
        for file in sorted(os.listdir(folder_path + folder)):
            with open(folder_path + folder + "/" + file, 'r') as myfile:
                file_data = myfile.read().replace('\n', ' ')
            file_name += (len(list(filter(None, file_data.split("##########")))) - 1) * [file]
            ocr_data = ocr_data + file_data + " "

directory_data = list(filter(None, ocr_data.split("##########")))   # list with each entry as an element in the list
directory_data.remove(directory_data[0])

nlp = spacy.load("en_core_web_lg")      # using spacy's predefined model

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe('ner')

for entry in directory_data:
    doc = nlp(entry)
    entities.append([(ent.text, ent.label_) for ent in doc.ents])   # extracting the labels for the entities

df = pd.DataFrame()       # creating a dataframe for tabular representation
df['file_name'] = pd.Series(file_name)
df['text'] = pd.Series(directory_data, index=df.index)
df['entities'] = pd.Series(entities, index=df.index)

for i in range(0, df.shape[0]):
    labels = df.loc[i]['entities']          # assigning an entity text under the correct column
    for label in labels:
        entity = label[1]
        if entity.lower() not in df:
            df[entity.lower()] = [[] for _ in range(len(df))]
            df.loc[i][entity.lower()].append(label[0])  # if more than one entities with the same label, then append to the list
        else:
            df.loc[i][entity.lower()].append(label[0])

df.to_csv('initial_ner.csv', index=False)   # producing a csv file
