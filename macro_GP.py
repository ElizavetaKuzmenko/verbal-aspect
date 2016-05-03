# coding:utf-8

import csv

# create macro GP for verb groups from PCA

groups = {}
with open('imperfectivity.csv') as ipf:
    reader = csv.reader(ipf, delimiter=',')
    header = next(reader)
    for row in reader:
        if 'i' + row[-1] in groups:
            groups['i' + row[-1]].add(row[0])
        else:
            groups['i' + row[-1]] = set([row[0]])

with open('perfectivity.csv') as pf:
    reader = csv.reader(pf, delimiter=',')
    header = next(reader)
    for row in reader:
        if 'p' + row[-1] in groups:
            groups['p' + row[-1]].add(row[0])
        else:
            groups['p' + row[-1]] = set([row[0]])

def write_groups():
    with open('groups.csv', 'w') as f:
        for group in groups:
            f.write(group + ',' + ','.join(groups[group]) + '\n')
    f.close()

m = open('macro_GP_absolute.csv', 'w')
writer = csv.writer(m, delimiter = ',', quotechar = '"')
header = ('group', 'praes', 'fut', 'praet', 'inf', 'imper', 'gerund',
          'partcp.act.past', 'partcp.act.nonpast', 'partcp.pass.past', 'partcp.pass.nonpast'
          )
writer.writerow(header)


for group in groups:
    with open('GP_absolute.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        print(group)
        praes = 0
        fut = 0
        praet = 0
        inf = 0
        imper = 0
        gerund = 0
        partcp_act_past = 0
        partcp_act_nonpast = 0
        partcp_pass_past = 0
        partcp_pass_nonpast = 0
        all = 0
        for row in reader:
            row[2:] = [float(i) for i in row[2:]]
            if row[0] + ' ' + row[1] in groups[group]:
                print(row[0])
                praes += row[2]
                fut += row[3]
                praet += row[4]
                inf += row[5]
                imper += row[6]
                gerund += row[7]
                partcp_act_past += row[8]
                partcp_act_nonpast += row[9]
                partcp_pass_past += row[10]
                partcp_pass_nonpast += row[11]
                all += row[12]
        try:
            all = 1
            row_write = (group, praes/all, fut/all, praet/all, inf/all, imper/all, gerund/all,
                partcp_act_past/all, partcp_act_nonpast/all, partcp_pass_past/all, partcp_pass_nonpast/all
                )
            writer.writerow(row_write)
        except ZeroDivisionError:
            pass
m.close()



