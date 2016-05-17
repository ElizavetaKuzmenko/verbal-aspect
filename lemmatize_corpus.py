# coding: utf-8

import lxml.etree as ET
import os, csv, codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

PATH_TO_CORPUS = os.path.join(os.getcwd(), 'source')
f = codecs.open('disamb_corpus.txt', 'w', 'utf-8')
stopwords = set([line.strip() for line in open('stopwords_ru')])

class Corpus():
    def __init__(self):
        self.sentences = set([])


    def load_file(self, path):
        print(path)
        """
        Open RNC XML and get all unique tokens
        """
        tree = ET.parse(path)
        for elem in tree.iter('p'):
            se = Sentence()
            words = elem.text.split(' ')
            for w in words:
                wf = w.strip('.,?!"\':;-()[]{}»«')
                if len(wf) == 0:
                    continue
                ana = morph.parse(wf)[0]
                pos = str(ana.tag).split(',')[0].split(' ')[0]
                lemma = ana.normal_form
                #wf = ''.join(elem.itertext()).lower().replace('`', '') # remove stress
                #for item in elem.iter('ana'):
                #    info = item
                #        #print(ET.tostring(info.getparent().getprevious(), encoding='utf-8'))
                #    break
                #lemma = [item.get("lex") for item in elem.iter('ana')] # todo: deal with homonymy?
                #lemma = info.get('lex')
                # get POS tag
                #pos = info.get("gr").split('=')[0].split(',')[0]
                word = Word(wf, lemma, pos)
                if word.pos != 'PNCT' and word.lemma not in stopwords:
                    se.words.append(word)
            if len(se.words) > 3:
                self.sentences.add(se)
                f.write(' '.join([word.lemma + '_' + word.pos for word in se.words]) + '\n')

    def load_dir(self, path):
        """
        Traverse a given directory and add all text files
        :param path: path to corpus folder
        """
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith('ml'):  # todo open all files, but throw warnings if they are not corpus files
                    try:
                        self.load_file(os.path.join(root, name))
                    except:
                          pass

class Word():
    def __init__(self, wf, lemma, pos):
        self.wf = wf
        self.lemma = lemma
        self.pos = pos

class Sentence():
    def __init__(self):
        self.words = []


def run():
    corpus = Corpus()
    corpus.load_dir(PATH_TO_CORPUS)
    f.close()
    #with open('disamb_corpus.txt', 'w', encoding='utf-8') as f:
    #    for sent in corpus.sentences:
    #        print(sent)
    #        f.write(' '.join([word.lemma + '_' + word.pos for word in sent.words]) + '\n')


if __name__ == '__main__':
    run()