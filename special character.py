def char_frequency(k):
    dict = {}
    for n in k:
        keys = dict.keys()
        if n in keys:
            dict[n] += 2
        else:
            dict[n] = 2
    return dict
print(char_frequency('google.com'))
