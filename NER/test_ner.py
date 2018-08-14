'''
This script tests the Named Entity Recognition model against the unannotated probate data. The model can be imported to test the remaining entries that are not annotated to extract the entities.

The input to the script is the folder containing the training model generated during the train_ner.py and a text file containing all the entries that need to be extracted.

To run the script:

python3 test_ner.py <path_to_model_directory> <path_to_test_data> <destination_path_for_files>

Dependencies:
1. SpaCy :
        pip3 install -U spacy

        Then, download and install a language model so that the semantics for the English language are used while training.

        python3 -m spacy download en
'''
import spacy
import sys
import pandas as pd
import os

entities = []
ocr_data = ""

model_name = sys.argv[1]
test_data = sys.argv[2]
output_directory = sys.argv[3]

if output_directory is not None:
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

model_name = model_name + "/" if (model_name[-1] is not '/') else model_name
output_directory = output_directory + "/" if (output_directory[-1] is not '/') else output_directory

with open(test_data) as myfile:
    directory_data = [x.replace('\n', ' ') for x in myfile]

print("Loading from", model_name)
nlp = spacy.load(model_name)            # loading the trained model
for entry in directory_data:
    doc = nlp(entry)                    # finding the ner entities
    entities.append([(ent.text, ent.label_) for ent in doc.ents])

df = pd.DataFrame()                     # creating a Pandas Dataframe
df['text'] = pd.Series(directory_data)

for i in range(0, len(entities)):
    labels = entities[i]
    for label in labels:
        entity = label[1]
        if entity.lower() not in df:
            df[entity.lower()] = [[] for _ in range(len(df))]
            df.loc[i][entity.lower()].append(label[0])          # adding entities
        else:
            df.loc[i][entity.lower()].append(label[0])

print("Saved .tsv, .csv and .xlsx files to ---> " + output_directory)
df.to_csv(output_directory + 'trained_ner.tsv', sep='\t', index=False)      # saving the files in different formats
df.to_csv(output_directory + 'trained_ner.csv', index=False)
df.to_excel(output_directory + 'trained_ner.xlsx', index=False)
