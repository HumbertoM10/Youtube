#!/usr/bin/python3

import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
import itertools
import isodate


def get_country_df(country):
    videos = pd.read_csv('./data/' + country + 'videos.csv')
    videos = videos[videos['comments_disabled'] == False]
    videos = videos[videos['ratings_disabled'] == False]
    videos['likes_log'] = np.log(videos['likes'] + 1)
    videos['views_log'] = np.log(videos['views'] + 1)
    videos['dislikes_log'] = np.log(videos['dislikes'] + 1)
    videos['comment_log'] = np.log(videos['comment_count'] + 1)
    encoding = pd.get_dummies(
        videos['category_id'], drop_first=True).add_suffix('_category')
    videos = videos.join(encoding)
    videos['category_name'] = np.nan
    videos.loc[(videos["category_id"] == 1),
               "category_name"] = 'Film and Animation'
    videos.loc[(videos["category_id"] == 2),
               "category_name"] = 'Cars and Vehicles'
    videos.loc[(videos["category_id"] == 10), "category_name"] = 'Music'
    videos.loc[(videos["category_id"] == 15),
               "category_name"] = 'Pets and Animals'
    videos.loc[(videos["category_id"] == 17), "category_name"] = 'Sport'
    videos.loc[(videos["category_id"] == 19),
               "category_name"] = 'Travel and Events'
    videos.loc[(videos["category_id"] == 20), "category_name"] = 'Gaming'
    videos.loc[(videos["category_id"] == 22),
               "category_name"] = 'People and Blogs'
    videos.loc[(videos["category_id"] == 23), "category_name"] = 'Comedy'
    videos.loc[(videos["category_id"] == 24),
               "category_name"] = 'Entertainment'
    videos.loc[(videos["category_id"] == 25),
               "category_name"] = 'News and Politics'
    videos.loc[(videos["category_id"] == 26),
               "category_name"] = 'How to and Style'
    videos.loc[(videos["category_id"] == 27), "category_name"] = 'Education'
    videos.loc[(videos["category_id"] == 28),
               "category_name"] = 'Science and Technology'
    videos.loc[(videos["category_id"] == 29),
               "category_name"] = 'Non Profits and Activism'
    videos.loc[(videos["category_id"] == 25),
               "category_name"] = 'News & Politics'
    videos['like_rate'] = videos['likes'] / videos['views'] * 100
    videos['dislike_rate'] = videos['dislikes'] / videos['views'] * 100
    videos['comment_rate'] = videos['comment_count'] / videos['views'] * 100
    videos['trending_date'] = pd.to_datetime(
        videos['trending_date'], format='%y.%d.%m')
    videos['publish_time'] = pd.to_datetime(
        videos['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
    videos['publish_time_full'] = pd.to_datetime(
        videos['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
    videos['time_to_trending'] = videos['trending_date'] - \
        videos['publish_time']
    videos['time_to_trending'] = [i.total_seconds()
                                  for i in videos['time_to_trending']]
    videos['pub_month'] = videos['publish_time'].dt.month
    videos['pub_julian'] = [
        i.timetuple().tm_yday for i in videos['publish_time']]
    videos.insert(4, 'publish_date', videos['publish_time'].dt.date)
    videos['publish_time'] = videos['publish_time'].dt.time
    videos[['pub_hour', 'pub_min', 'pub_sec']] = videos['publish_time'].astype(
        str).str.split(':', expand=True).astype(int)

    durations = pd.read_csv('./scraps/duration' + country + '.csv')
    durdic = {
        row['video_id']:
        (
            isodate.parse_duration(row['duration']).total_seconds()
            if str(row['duration']) != 'nan'
            else None
        )
        for index, row in durations.iterrows()
    }
    videos['duration'] = [(durdic[row['video_id']] if row['video_id'] in durdic.keys() else None) for index, row in videos.iterrows()]
    videos.dropna(subset=['duration'], inplace=True)
    return videos

def getX_y(country, targets):
    df = get_country_df(country)
    user_ins = [
        # 'comments_disabled',
        # 'ratings_disabled',
        '2_category',
        '10_category', '15_category', '17_category', '19_category',
        '20_category', '22_category', '23_category', '24_category',
        '25_category', '26_category', '27_category', '28_category',
        '29_category', '43_category', 'pub_julian',
        'pub_month', 'pub_hour', 'pub_min',# 'pub_sec',
        'duration'
    ]
    X = df[user_ins]
    y = df[targets]
    return X, y
