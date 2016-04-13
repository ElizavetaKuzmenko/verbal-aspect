# coding: utf-8

import sqlite3, re, lxml.html

PATH_TO_BASE = '/home/lizaku/Документы/Big_Data/zal.db3'
PATH_TO_HTML = '/home/lizaku/PycharmProjects/verbal-aspect/prefixal.html'

base = sqlite3.connect(PATH_TO_BASE)
c = base.cursor()
re_lat = re.compile('[a-zA-Z]')

def suffixal():
    #SELECT source FROM headword JOIN descriptor ON descriptor.word_id=headword.id
    # SELECT descriptor_id FROM aspect_pair
    c.execute('SELECT source FROM headword JOIN descriptor ON descriptor.word_id=headword.id WHERE descriptor.id IN '
              '(SELECT descriptor_id FROM aspect_pair)')
    with open('verbs_zal.txt', 'w') as f:
        for i in c.fetchall():
            f.write(i[0] + '\n')


def prefixal():
    with open(PATH_TO_HTML, 'r', encoding='utf-8') as f:
        html = f.read()
    root = lxml.html.fromstring(html)
    rows = root.xpath(u'//table[contains(@cellpadding, "5")]/tr') + ['\n']
    with open('verbs_prefixes.csv', 'w') as f:
        for row in rows[0][0]:
            cells = row.xpath('//td//a/text()')
            cells = [cell for cell in cells if re_lat.search(cell) is None]
            cell_groups = zip(*(iter(cells),) * 3)
            for group in cell_groups:
                f.write(','.join(group) + '\n')




if __name__ == '__main__':
    #suffixal()
    prefixal()
