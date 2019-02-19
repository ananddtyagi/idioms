from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from googletrans import Translator
import string
translator = Translator()
import csv
from clean import filter

def findIdioms(phrase):
    input = phrase

    detected = translator.detect(input)

    lang = detected.lang
    t = translator.translate(input, src = lang).text
    print("translation:", t)
    t = filter(t).lower().replace(" ", "")

    f = open('idioms.csv')
    csv_f = csv.reader(f)
    matches = []
    idiom = ""
    found = False
    for row in csv_f:
        if row[2].lower().replace(" ", "") == t:
            matches.append(row[0])
            found = True
    matches = list(set(matches))
    ret = []
    if found:
        ret.append(True)
        ret.append("Here are list of English idioms that are similar in meaning:")
        for m in matches:
            ret.append(m)
    if not found:
        ret.append(False)
        ret.append("Unfortunately, no matches were found")
        ret.append("This is the translation of the phrase in English: " + t)

    f.close()
    return ret
