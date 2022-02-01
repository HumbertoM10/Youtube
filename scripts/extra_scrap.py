#!/usr/bin/python3

import pandas as pd
import requests

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

key = 'AIzaSyD7aumbqlL9DbCOsh42wPLtZnDFIQzKTkc'
videos = pd.read_csv('./data/MXvideos.csv',usecols=[0])

print('[')
for i in chunks(videos['video_id'], 50):
    url = 'https://www.googleapis.com/youtube/v3/videos?id=' + ','.join(i) + '&part=contentDetails&key=' + key
    response = requests.get(url)
    print(response.text, ',')
#     break
print(']')
