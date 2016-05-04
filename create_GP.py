# coding: utf-8
import csv

# 'token', 'lemma', 'aspect', 'form', 'transitivity', 'number', 'tense', 'mood', 'person', 'voice'
# Read the data from the feature matrix and create grammatical profiles (absolute and relative)

def GP_all():
    freq_dic = {}
    with open('feature_matrix.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)

        for row in reader:
            parameters = [x for x in [row[3], row[6], row[7], row[9]] if x != 'None']
            aspect = row[2]
            lemma = row[1]
            if (lemma, aspect) not in freq_dic:
                #print(row[1])
                freq_dic[(lemma, aspect)] = {'_'.join(parameters): 1}
            else:
                #print(lemma)
                try:
                    freq_dic[(lemma, aspect)]['_'.join(parameters)] += 1
                except KeyError:
                    freq_dic[(lemma, aspect)]['_'.join(parameters)] = 1

    print(len(freq_dic))

    #with open('grammatical_profiles.csv', 'w', encoding='utf-8') as f:
    #    HEADER = ('lemma', 'form', 'frequency')
    #    writer = csv.writer(f, delimiter=',', quotechar='"')
    #    writer.writerow(HEADER)
    #    for k in sorted(freq_dic):
    #        for y in sorted(freq_dic[k], key=lambda y: -freq_dic[k][y]):
    #            row = (k[0], k[1], y, freq_dic[k][y])
    #            writer.writerow(row)


def GP_relative():
    with open('feature_matrix.csv', 'r', encoding='utf-8') as f:
        all_verbs = len(f.readlines()) - 1
    with open('feature_matrix.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        freq_dic = {}
        for row in reader:
            lemma, aspect, form = row[1:4]
            tense, mood = row[6:8]
            voice = row[-1]
            if (lemma, aspect) not in freq_dic:
                freq_dic[(lemma, aspect)] = {'nonpast': 0, 'praet': 0, 'inf': 0, 'imper': 0, 'gerund': 0,
                                             'partcp.act.past': 0, 'partcp.act.nonpast': 0, 'partcp.pass.past': 0,
                                             'partcp.pass.nonpast': 0}
            if form == 'fin':
                if mood != 'imper':
                    if tense == 'praet':
                        freq_dic[(lemma, aspect)]['praet'] += 1
                    elif tense == 'praes':
                        freq_dic[(lemma, aspect)]['nonpast'] += 1
                    elif tense == 'fut':
                        freq_dic[(lemma, aspect)]['nonpast'] += 1
                    else:
                        print('tense', row)
                elif mood == 'imper':
                    freq_dic[(lemma, aspect)]['imper'] += 1
            elif form == 'inf':
                freq_dic[(lemma, aspect)]['inf'] += 1
            elif form == 'ger':
                freq_dic[(lemma, aspect)]['gerund'] += 1
            elif form == 'partcp':
                if voice == 'pass' and tense != 'praet':
                    freq_dic[(lemma, aspect)]['partcp.pass.nonpast'] += 1
                elif voice == 'act' and tense != 'praet':
                    freq_dic[(lemma, aspect)]['partcp.act.nonpast'] += 1
                elif voice == 'pass' and tense == 'praet':
                    freq_dic[(lemma, aspect)]['partcp.pass.past'] += 1
                elif voice == 'act' and tense == 'praet':
                    freq_dic[(lemma, aspect)]['partcp.act.past'] += 1
                else:
                    # todo: med voice!!
                    print('partcp', row)
            else:
                print('form', row)
    with open('GP_absolute.csv', 'w', encoding='utf-8') as f:
        HEADER = ('lemma', 'aspect', 'nonpast', 'past', 'inf', 'imper', 'gerund',
                  'partcp.act.past', 'partcp.act.nonpast', 'partcp.pass.past', 'partcp.pass.nonpast')
        writer = csv.writer(f, delimiter=',', quotechar='"')
        writer.writerow(HEADER)
        for verb in sorted(freq_dic):
            all = sum([
                      freq_dic[verb]['nonpast'], freq_dic[verb]['praet'],
                      freq_dic[verb]['inf'], freq_dic[verb]['imper'], freq_dic[verb]['gerund'],
                      freq_dic[verb]['partcp.act.past'],
                      freq_dic[verb]['partcp.act.nonpast'], freq_dic[verb]['partcp.pass.past'],
                      freq_dic[verb]['partcp.pass.nonpast']
                      ])
            if all < 100:
                continue
            # for absolute figures!
            all = 1
            try:
                row = (verb[0], verb[1], freq_dic[verb]['nonpast']/all, freq_dic[verb]['praet']/all,
                       freq_dic[verb]['inf']/all, freq_dic[verb]['imper']/all, freq_dic[verb]['gerund']/all,
                       freq_dic[verb]['partcp.act.past']/all, freq_dic[verb]['partcp.act.nonpast']/all,
                       freq_dic[verb]['partcp.pass.past']/all, freq_dic[verb]['partcp.pass.nonpast']/all
                       )
                writer.writerow(row)
            except ZeroDivisionError:
                print(all, verb, freq_dic[verb])


if __name__ == '__main__':
    GP_relative()