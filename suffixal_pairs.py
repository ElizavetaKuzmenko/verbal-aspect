# coding: utf-8

import sqlite3

PATH_TO_BASE = '/home/lizaku/Документы/Big_Data/zal.db3'

base = sqlite3.connect(PATH_TO_BASE)
c = base.cursor()

def extract_pairs():
    #SELECT source FROM headword JOIN descriptor ON descriptor.word_id=headword.id
    # SELECT descriptor_id FROM aspect_pair
    c.execute('SELECT source FROM headword JOIN descriptor ON descriptor.word_id=headword.id WHERE descriptor.id IN '
              '(SELECT descriptor_id FROM aspect_pair)')
    with open('verbs_zal.txt', 'w') as f:
        for i in c.fetchall():
            f.write(i[0] + '\n')

if __name__ == '__main__':
    extract_pairs()
