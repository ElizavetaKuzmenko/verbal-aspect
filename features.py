# coding: utf-8

def get_features(info):
    gr = info.get('gr')
    features = []

    ''' aspect '''
    if 'pf' in gr:
        aspect = 'pf'
    elif 'ipf' in gr:
        aspect = 'ipf'
    else:
        aspect = None
    features.append(aspect)

    ''' tense '''
    if 'praes' in gr:
        tense = 'praes'
    elif 'praet' in gr:
        tense = 'praet'
    elif 'fut' in gr:
        tense = 'fut'
    else:
        tense = None
    features.append(tense)

    ''' transitivity '''
    if 'tran' in gr:
        trans = 'tran'
    elif 'intr' in gr:
        trans = 'intr'
    else:
        trans = None
    features.append(trans)

    ''' voice '''
    if 'act' in gr:
        voice = 'act'
    elif 'pass' in gr:
        voice = 'pass'
    elif 'med' in gr:
        voice = 'med'
    else:
        voice = None
    features.append(voice)

    ''' form '''
    if 'inf' in gr:
        form = 'inf'
    elif 'partcp' in gr:
        form = 'partcp'
    elif 'ger' in gr:
        form = 'ger'
    else:
        form = 'fin'
    features.append(form)

    ''' mood '''
    if 'indic' in gr:
        mood = 'indic'
    elif 'imper' in gr:
        mood = 'imper'
    else:
        mood = None
    features.append(mood)

    ''' person '''
    if '1p' in gr:
        pers = '1'
    elif '2p' in gr:
        pers = '2'
    elif '3p' in gr:
        pers = '3'
    else:
        pers = None
    features.append(pers)

    ''' number '''
    if 'sg' in gr:
        num = 'sg'
    elif 'pl' in gr:
        num = 'pl'
    else:
        num = None
    features.append(num)

    return features