import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

leammatizer = WordNetLemmatizer()


def get_intents(intents_filepath):
    return json.loads(open(intents_filepath).read())


def clean_up_sentence(sentence: str) -> list:
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [leammatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def sent_to_bow_array(sentence: str, words):
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
