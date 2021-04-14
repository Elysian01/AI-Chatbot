import warnings
import random
import nltk
import pickle

import numpy as np
from termcolor import colored
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

import config
words_filename, tags_filename, model_filename = config.get_filenames()

warnings.filterwarnings("ignore")


leammatizer = WordNetLemmatizer()
intents = config.get_intents()

# Loading words, tags and model
words = pickle.load(open(words_filename, "rb"))
tags = pickle.load(open(tags_filename, "rb"))
model = load_model(model_filename)


def clean_up_sentence(sentence: str) -> list:
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [leammatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence: str):
    """
    Convert sentence into bow array
    """
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for sentence_word in sentence_words:
        for i, word_list in enumerate(words):
            if word_list == sentence_word:
                bag[i] = 1

    return np.array([bag])


def predict_tag(sentence: str, ERROR_THRESHOLD=0.25) -> list:
    bow = bag_of_words(sentence)
    res = model.predict(bow)[0]
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)  # sort by prob

    return_list = []
    for r in results:
        return_list.append(
            {
                "intent": tags[r[0]],
                "probability": str(r[1])
            })

    return return_list


def get_response(intents_list, intents_json):
    # since sorted according to prob, 1st => highest
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i["responses"])
            break
    return result


if __name__ == "__main__":
    print(colored("\nBot is online, start conversation....\n", "red"))
    end_conversation = ["/stop", "exit"]

    while True:
        message = input("> ")

        if message in end_conversation:
            print("Thankyou for your time :)")
            break

        intents_list = predict_tag(message)
        response = get_response(intents_list, intents)
        print(colored(response, "blue"))
