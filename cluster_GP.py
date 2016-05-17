# coding: utf-8

import csv

# sort verbs by their position on the plot

def write_cats():
    ipf = {}
    pf = {}
    with open('GP_scores.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        for row in reader:
            if -0.1 <= float(row[2]) <= 0.1 and -0.1 <= float(row[1]) <= 0.1:
                ipf[row[0]] = (float(row[1]), float(row[2]), 2)
            #if float(row[2]) >= 0:
            #    if 0 <= float(row[2]) < 0.1:
            #        ipf[row[0]] = (float(row[1]), float(row[2]), 1)
            #    elif 0.1 <= float(row[2]) < 0.25:
            #        ipf[row[0]] = (float(row[1]), float(row[2]), 2)
            #    else:
            #        ipf[row[0]] = (float(row[1]), float(row[2]), 3)
            #else:
            #    if float(row[2]) > -0.25:
            #        pf[row[0]] = (float(row[1]), float(row[2]), 1)
            #    elif -0.25 >= float(row[1]) > -0.5:
            #        pf[row[0]] = (float(row[1]), float(row[2]), 2)
            #    else:
            #        pf[row[0]] = (float(row[1]), float(row[2]), 3)

    print(len(ipf) + len(pf))

    with open('imperfectivity.csv', 'w', encoding='utf-8') as f:
        HEADER = ('verb', 'factor1', 'factor2', 'group')
        writer = csv.writer(f, delimiter=',', quotechar='"')
        writer.writerow(HEADER)
        for verb in sorted(ipf, key=lambda k: ipf[k][1]):
            #print(verb)
            row = (verb, ipf[verb][0], ipf[verb][1], ipf[verb][2])
            writer.writerow(row)

    with open('perfectivity.csv', 'w', encoding='utf-8') as f:
        HEADER = ('verb', 'factor1', 'factor2', 'group')
        writer = csv.writer(f, delimiter=',', quotechar='"')
        writer.writerow(HEADER)
        for verb in sorted(pf, key=lambda k: pf[k][1]):
            #print(verb)
            row = (verb, pf[verb][0], pf[verb][1], pf[verb][2])
            writer.writerow(row)


if __name__ == '__main__':
    write_cats()