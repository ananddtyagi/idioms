from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from googletrans import Translator
import string
translator = Translator()
import csv
import pandas as pd

contractions = {
    "\'s":"is",
    "\'re": "are",
    "n\'t":"not",
    "\'ll":"will",
    "\'ve":"have"
}
def filter(sent): #returns the filter, but seperates words with approstrophese
#change this so that it switches the approstrophy to the long version of the word
    example_sent = sent

    word_tokens = word_tokenize(example_sent)

    filtered_sentence = [w for w in word_tokens]

    filtered_sentence = []

    for w in word_tokens:
        if("\'" in w):
            try:
                w = contractions[w]
            except:
                print("fail",w)
        filtered_sentence.append(w)
    str = ' '.join(filtered_sentence)
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)
    return str
