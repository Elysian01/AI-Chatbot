from aichatbot import utils
import random
import nltk
import pickle

import numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD


def train_bow_model(filenames, print_summary=False):

    intents_file_path, words_file_path, tags_file_path, model_file_path = \
        filenames['intents'], filenames['words'], filenames['tags'], filenames['model']

    leammatizer = WordNetLemmatizer()
    intents = utils.get_intents(intents_file_path)

    words = []
    tags = []
    documents = []  # contains tuple of (word list and tag names)
    ignore_letters = ["?", "!", ".", ","]

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent["tag"]))

            if intent["tag"] not in tags:
                tags.append(intent["tag"])

    # print(documents)

    # Preprocess document
    print("Preprocessing data ....")
    words = [leammatizer.lemmatize(word)
             for word in words if word not in ignore_letters]
    words = sorted(set(words))

    # print(words)

    tags = sorted(set(tags))

    # Saving word and tags
    print("Saving words and tags in pickle file ...")
    pickle.dump(words, open(words_file_path, "wb"))
    pickle.dump(tags, open(tags_file_path, "wb"))

    training = []
    output_empty = [0] * len(tags)

    for document in documents:
        bag = []
        word_pattern = document[0]
        word_pattern = [leammatizer.lemmatize(
            word.lower()) for word in word_pattern]
        for word in words:
            bag.append(1) if word in word_pattern else bag.append(0)

        output_row = list(output_empty)
        output_row[tags.index(document[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    # Building Model
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]), ), activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation="softmax"))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.5, nesterov=True)

    model.compile(loss="categorical_crossentropy",
                  optimizer=sgd, metrics=["accuracy"])

    if print_summary:
        print(model.summary())

    print("Training Started ...")
    hist = model.fit(np.array(train_x), np.array(train_y),
                     epochs=200, batch_size=5, verbose=1)
    model.save(model_file_path, hist)

    print("Model Training Completed!")
    print("Model Saved having loacation: ", model_file_path)

    return model


if __name__ == "__main__":
    pass
