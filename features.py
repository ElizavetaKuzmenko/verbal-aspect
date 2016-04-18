# coding: utf-8


def get_features(info, info_prev):
    gr = info.get('gr')
    if info_prev is not None:
        lex_prev = info_prev.get('lex')
    else:
        lex_prev = None
    features = []

    ''' aspect '''
    if 'ipf' in gr:
        aspect = 'ipf'
    elif 'pf' in gr:
        aspect = 'pf'
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
    if 'inf' in gr and lex_prev != 'быть':
        form = 'inf'
    elif lex_prev == 'быть':
        features[1] = 'fut'
        gr_prev = info_prev.get('gr')
        if 'sg' in gr_prev:
            features[3] = 'sg'
        elif 'pl' in gr_prev:
            features[3] = 'pl'
        if '1p' in gr_prev:
            features[2] = '1'
        elif '2p' in gr_prev:
            features[2] = '2'
        elif '3p' in gr_prev:
            features[2] = '3'
        form = 'fin'
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

    # to avoid empty cells because of NoneType
    features = [str(f) for f in features]
    return features