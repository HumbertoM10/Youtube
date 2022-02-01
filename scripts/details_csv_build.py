#!/usr/bin/python3

import pandas as pd

import json

with open('scraps/contentDetailsMX.json') as json_file:
    data = json.load(json_file)
    print('video_id,duration')
    for vid50 in data:
        for video in vid50['items']:
            # print(video)
            print(video['id'] + ',' + (video['contentDetails']['duration'] if 'contentDetails' in video.keys() else ''))