# coding: utf-8

import os, re
import lxml.etree as ET
from get_features_RNC import get_features
import csv
from pymystem3 import Mystem
m = Mystem()

# analyze RNC with mystem and print all the data in a big table

PATH_TO_CORPUS = os.path.join(os.getcwd(), 'source/post1950')
errors = open('Parse_errors.txt', 'w')
RNC_f = open('feature_matrix_big.csv', 'w')


def mystem(sentence):
    sentence = sentence.strip()
    anas = m.analyze(sentence)
    return anas


class Verb():
    def __init__(self, lemma, wf, aspect, tense, person, number, trans, voice, form, mood):
        self.lemma = lemma
        self.wf = wf
        self.form = form
        self.aspect = aspect
        self.transitivity = trans
        self.number = number
        self.tense = tense
        self.mood = mood
        self.person = person
        self.voice = voice


def load_file(path):
    print(path)
    """
    Open RNC XML and get all unique tokens
    """
    verbs = []
    tree = ET.parse(path)
    for elem in tree.iter('p'):
        paragraph = ''.join(elem.itertext()).lower()
        sentences = re.split(r'(?:[.]\s*){3}|[.?!]', paragraph)
        for sentence in sentences:
            anas = mystem(sentence)
            anas = [ana for ana in anas if 'analysis' in ana and ana['analysis'] != []]
            for ana in anas:
                #print(ana)
                info = ana['analysis'][0]['gr']
                tag = info.split('=')[0].split(',')[0]
                lemma = ana['analysis'][0]['lex']
                word = ana['text']
                if tag == 'V':
                    features = get_features(info)
                    verb = Verb(lemma, word, *features)
                    verbs.append(verb)
    return verbs


def to_csv(verbs):
    """
    Write featurized verbs to csv file
    """
    HEADER = ('token', 'lemma', 'aspect', 'form', 'transitivity',
              'number', 'tense', 'mood', 'person', 'voice')
    writer = csv.writer(RNC_f, delimiter=',', quotechar='"')
    writer.writerow(HEADER)

    for verb in verbs:
        row = (
            verb.wf, verb.lemma, verb.aspect, verb.form, verb.transitivity,
            verb.number, verb.tense, verb.mood, verb.person, verb.voice
            )
        writer.writerow(row)


def load_dir(path):
    """
    Traverse a given directory and add all text files
    :param path: path to corpus folder
    """
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('ml'):
                # todo open all files, but throw warnings if they are not corpus files
                verbs = load_file(os.path.join(root, name))
                to_csv(verbs)


def run():
    load_dir(PATH_TO_CORPUS)
    RNC_f.close()


if __name__ == '__main__':
    run()

