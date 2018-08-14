'''
Creates NER training data in SpaCy format from JSON downloaded from Dataturks.Once you download the JSON file from Dataturks, you can load it using the python script and outputs the training data in a pickle file having a format which can be used for training using SpaCy.

A pickle file serializes objects so they can be saved to a file, and loaded in a program again later on. It has an extension of *.pkl.

To run the script:

python3 dataturks_to_spacy.py <path_to_json_file> <destination_path>
'''
import json
import sys
import os
import pickle


def convert_dataturks_to_spacy(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines = []
        with open(dataturks_JSON_FilePath, 'r') as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            text = data['content']
            entities = []
            for annotation in data['annotation']:
                # only a single point in text annotation.
                point = annotation['points'][0]
                labels = annotation['label']
                # handle both list of labels or a single label.
                if not isinstance(labels, list):
                    labels = [labels]

                for label in labels:
                    # dataturks indices are both inclusive [start, end] but spacy is not [start, end)
                    entities.append((point['start'], point['end'] + 1, label))

            training_data.append((text, {"entities": entities}))

        return training_data
    except Exception as e:
        print("Unable to process " + dataturks_JSON_FilePath + "\n" + "error = " + str(e))
        return None


if __name__ == '__main__':
    dataturks_JSON_FilePath = sys.argv[1]
    training_output_Path = sys.argv[2]

    if training_output_Path is not None:
        if not os.path.exists(training_output_Path):
            os.mkdir(training_output_Path)

    training_output_Path = training_output_Path + "/" if (training_output_Path[-1] is not '/') else training_output_Path
    training_data = convert_dataturks_to_spacy(dataturks_JSON_FilePath)

    with open(training_output_Path + "training_data.pkl", 'wb') as output:
        pickle.dump(training_data, output, pickle.HIGHEST_PROTOCOL)

    print("Pickle file \"training_data.pkl\" saved to ---> " + training_output_Path)
