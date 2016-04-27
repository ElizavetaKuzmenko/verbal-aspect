# coding: utf-8


def get_features(gr):
    features = []

    ''' aspect '''
    if 'несов' in gr:
        aspect = 'ipf'
    elif 'сов' in gr:
        aspect = 'pf'
    else:
        aspect = None
    features.append(aspect)

    ''' tense '''
    if 'непрош' in gr:
        tense = 'praes'
    elif 'прош' in gr:
        tense = 'praet'
    else:
        tense = None
    features.append(tense)

    ''' person '''
    if '1-л' in gr:
        pers = '1'
    elif '2-л' in gr:
        pers = '2'
    elif '3-л' in gr:
        pers = '3'
    else:
        pers = None
    features.append(pers)

    ''' number '''
    if 'ед' in gr:
        num = 'sg'
    elif 'мн' in gr:
        num = 'pl'
    else:
        num = None
    features.append(num)

    ''' transitivity '''
    if 'пе' in gr:
        trans = 'tran'
    elif 'нп' in gr:
        trans = 'intr'
    else:
        trans = None
    features.append(trans)

    ''' voice '''
    if 'действ' in gr:
        voice = 'act'
    elif 'страд' in gr:
        voice = 'pass'
    elif 'мед' in gr:
        voice = 'med'
    else:
        voice = None
    features.append(voice)

    ''' form '''
    if 'инф' in gr:
        form = 'inf'
    elif 'прич' in gr:
        form = 'partcp'
    elif 'деепр' in gr:
        form = 'ger'
    else:
        form = 'fin'
    features.append(form)

    ''' mood '''
    if 'изъяв' in gr:
        mood = 'indic'
    elif 'пов' in gr:
        mood = 'imper'
    else:
        mood = None
    features.append(mood)

    # to avoid empty cells because of NoneType
    features = [str(f) for f in features]
    return features