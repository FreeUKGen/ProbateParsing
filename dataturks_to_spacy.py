'''
Creates NER training data in Spacy format from JSON downloaded from Dataturks.

Outputs the Spacy training data which can be used for Spacy training.
'''
import json
import sys
import logging
import pickle


def convert_dataturks_to_spacy(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines = []
        with open(dataturks_JSON_FilePath, 'r') as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            print(len(data))
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
        logging.exception("Unable to process " + dataturks_JSON_FilePath + "\n" + "error = " + str(e))
        return None


if __name__ == '__main__':
    dataturks_JSON_FilePath = sys.argv[1]
    training_output_FilePath = sys.argv[2]
    training_data = convert_dataturks_to_spacy(dataturks_JSON_FilePath)
    print(training_data)
    with open(training_output_FilePath, 'wb') as output:
        pickle.dump(training_data, output, pickle.HIGHEST_PROTOCOL)
