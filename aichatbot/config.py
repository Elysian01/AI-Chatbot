import json


# intents_filename = "./data/bash_intents.json"
intents_filename = "./data/basic_intents.json"


words_filename = "./dumps/words.pkl"
tags_filename = "./dumps/tags.pkl"
model_filename = "./dumps/chatbot_model.h5"


def get_intents():
    return json.loads(open(intents_filename).read())


def get_filenames():
    """
    return filenames of words, tags and model
    """
    return words_filename, tags_filename, model_filename
