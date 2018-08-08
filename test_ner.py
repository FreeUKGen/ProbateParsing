import spacy
import sys
import pandas as pd


entities = []
ocr_data = ""
test_data = sys.argv[2]
model_name = sys.argv[1]

with open(test_data) as myfile:
    directory_data = [x.replace('\n', ' ') for x in myfile]

print(directory_data)
print("Loading from", model_name)
nlp = spacy.load(model_name)
for entry in directory_data:
    doc = nlp(entry)
    entities.append([(ent.text, ent.label_) for ent in doc.ents])

print(entities)
df = pd.DataFrame()
# df['file_name'] = pd.Series(file_name)
df['text'] = pd.Series(directory_data)
df['entities'] = pd.Series(entities, index=df.index)

for i in range(0, len(entities)):
    labels = df.loc[i]['entities']
    for label in labels:
        print(label)
        entity = label[1]
        if entity.lower() not in df:
            print("entered if")
            df[entity.lower()] = [[] for _ in range(len(df))]
            df.loc[i][entity.lower()].append(label[0])
        else:
            print("entered else")
            df.loc[i][entity.lower()].append(label[0])

df.to_csv('trained_ner.csv', index=False)
