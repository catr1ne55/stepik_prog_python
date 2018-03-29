def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] += [value]
    else:
        nkey = 2 * key
        if nkey in d.keys():
            d[nkey] += [value]
        else:
            d.update({nkey:[value]})