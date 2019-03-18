from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from googletrans import Translator
from fuzzywuzzy import fuzz
import string

import csv
from clean import filter

def findIdioms(phrase):
    input = phrase
    translator = Translator()
    detected = translator.detect(input)
    print("DETECTED ", detected.lang)
    lang = detected.lang
    if lang == "jazh-CN":
        lang = "zh-CN" #issue with Japanese vs Chinese
    t = translator.translate(input, src = lang).text
    print("translation:", t)
    t = filter(t)

    f = open('idioms.csv')
    csv_f = csv.reader(f)
    matches = []
    idiom = ""
    found = False
    for row in csv_f:
        if fuzz.token_set_ratio(row[2],t) > 75: #replaced an exact match with a fuzzy string comparison
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
