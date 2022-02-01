#!/usr/bin/python3

import pandas as pd

def maxrate(X, Y):
    maxr = X.iloc[0]
    maxp = Y[0]
    for i in range(len(X)):
        if Y[i] > maxp:
            maxp = Y[i]
            maxr = X.iloc[i]

    # for index, row in Y.iterrows():
    #     result += str(row['pub_hour']) + ':' + str(row['pub_min']) + '\n'
    return str(maxr['pub_hour']).zfill(2) + ':' + str(maxr['pub_min']).zfill(2) + '\n'

def minrate(X, Y):
    maxr = X.iloc[0]
    maxp = Y[0]
    for i in range(len(X)):
        if Y[i] < maxp:
            maxp = Y[i]
            maxr = X.iloc[i]
    return str(maxr['pub_hour']).zfill(2) + ':' + str(maxr['pub_min']).zfill(2) + '\n'

def get_best(X, Y, target):
    rule = {
        'like_rate': maxrate, 'dislike_rate': maxrate,
        'comment_rate': maxrate, 'time_to_trending': minrate,
        'views': maxrate
    }
    return rule[target](X, Y)