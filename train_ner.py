'''
This script trains the Named Entity Recognition model and returns the trained model on the probate wills annotated data. The model can be imported to test the remaining entries that are not annotated to extract the entities.

The input to the script is the pickle file generated during the dataturks_to_spacy.py.

To run the script:

python3 train_ner.py <path_to_pickle_file> <model_destination_path>

Dependencies:
1. SpaCy :
        pip3 install -U spacy

        Then, download and install a language model so that the semantics for the English language are used while training.

        python3 -m spacy download en

'''

import pickle
import spacy
import random
import sys
import os


def train_spacy(training_pickle_file, output_dir):

    # read pickle file to load training data
    with open(training_pickle_file, 'rb') as input:
        TRAIN_DATA = pickle.load(input)

    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(10):        # you can change the number of iteration for training
            print("Starting iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)

    # save model to output directory
    if output_dir is not None:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        nlp.meta['name'] = "probate_ner"  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to \"training_model\" at --->", output_dir)


if __name__ == "__main__":
    training_pickle_file = sys.argv[1]
    output_directory = sys.argv[2]

    if output_directory is not None:
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)

    output_directory = output_directory + "/" if (output_directory[-1] is not '/') else output_directory

    train_spacy(training_pickle_file, output_directory)
