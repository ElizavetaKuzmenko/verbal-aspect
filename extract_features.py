# coding: utf-8

import lxml.etree as ET
import os, csv
from features import get_features

PATH_TO_CORPUS = 'texts'
PATH_TO_VERBS = ['verbs_prefixes.csv', 'verbs_zal.txt']

class Corpus():
    def __init__(self):
        self.verbs = set([])
        self.partcp = set([])
        self.gerund = set([])


    def load_file(self, path, verbs):
        print(path)
        """
        Open RNC XML and get all unique tokens
        """
        tree = ET.parse(path)
        for elem in tree.iter('w'):
            word = ''.join(elem.itertext()).lower().replace('`', '') # remove stress
            for item in elem.iter('ana'):
                info = item
                try:
                    info_prev = [t for t in info.getparent().getprevious() if t.tag == 'ana'][0]
                except TypeError:
                    info_prev = None
                except IndexError:
                    info_prev = None
                    #print(ET.tostring(info.getparent().getprevious(), encoding='utf-8'))
                break
            #lemma = [item.get("lex") for item in elem.iter('ana')] # todo: deal with homonymy?
            lemma = info.get('lex')
            # get POS tag
            tag = info.get("gr").split('=')[0].split(',')[0]
            if lemma in verbs and tag == 'V':
                features = get_features(info, info_prev)
                verb = Verb(lemma, word, *features)
                if verb.form == 'partcp':
                    self.partcp.add(verb)
                elif verb.form == 'ger':
                    self.gerund.add(verb)
                self.verbs.add(verb)


    def load_dir(self, path, verbs):
        """
        Traverse a given directory and add all text files
        :param path: path to corpus folder
        """
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith('ml'):  # todo open all files, but throw warnings if they are not corpus files
                    self.load_file(os.path.join(root, name), verbs)

    def to_csv(self):
        """
        Write featurized verbs to csv file
        """
        HEADER = ('token', 'lemma', 'aspect', 'form', 'transitivity',
                  'number', 'tense', 'mood', 'person', 'voice')
        with open('feature_matrix.csv', 'w') as out:
            writer = csv.writer(out, delimiter=',', quotechar='"')
            writer.writerow(HEADER)

            for verb in self.verbs:
                row = (
                    verb.wf, verb.lemma, verb.aspect, verb.form, verb.transitivity,
                    verb.number, verb.tense, verb.mood, verb.person, verb.voice
                )
                writer.writerow(row)

    def participles(self):
        """
            Write featurized participles to csv file for inspection
            """
        HEADER = ('token', 'lemma', 'aspect', 'form', 'transitivity',
                  'number', 'tense', 'mood', 'person', 'voice')
        with open('participles.csv', 'w') as out:
            writer = csv.writer(out, delimiter=',', quotechar='"')
            writer.writerow(HEADER)

            for verb in self.partcp:
                row = (
                    verb.wf, verb.lemma, verb.aspect, verb.form, verb.transitivity,
                    verb.number, verb.tense, verb.mood, verb.person, verb.voice
                )
                writer.writerow(row)

    def gerunds(self):
        """
            Write featurized gerunds to csv file for inspection
            """
        HEADER = ('token', 'lemma', 'aspect', 'form', 'transitivity',
                  'number', 'tense', 'mood', 'person', 'voice')
        with open('gerunds.csv', 'w') as out:
            writer = csv.writer(out, delimiter=',', quotechar='"')
            writer.writerow(HEADER)

            for verb in self.gerund:
                row = (
                    verb.wf, verb.lemma, verb.aspect, verb.form, verb.transitivity,
                    verb.number, verb.tense, verb.mood, verb.person, verb.voice
                )
                writer.writerow(row)

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


def load_verbs(path):
    verbs = set()
    with open(path[0]) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            verbs.add(row[0])
            verbs.add(row[1])
    with open(path[1]) as f:
        for line in f:
            verbs.add(line.strip())
    return verbs



def run():
    verbs = load_verbs(PATH_TO_VERBS)
    corpus = Corpus()
    corpus.load_dir(os.path.join(os.getcwd(), PATH_TO_CORPUS), verbs)
    corpus.to_csv()
    corpus.participles()
    corpus.gerunds()



if __name__ == '__main__':
    # test()
    run()