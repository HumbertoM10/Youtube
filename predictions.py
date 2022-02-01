#!/usr/bin/python3

import numpy as np
import pandas as pd
# from sklearn import datasets
# import seaborn as sns
# from sklearn.feature_selection import RFE
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt

# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import ElasticNet
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor

# from sklearn.model_selection import GridSearchCV

# from sklearn.metrics import mean_squared_error
import datetime

# import data_process

def req_to_rows(req):
    pubday = datetime.datetime(2019, int(req['month']), int(req['day']))
    tt = pubday.timetuple()
    template = {
        # 'comments_disabled': req['comments_disabled'] == 'true',
        # 'ratings_disabled': req['ratings_disabled'] == 'true',
        '2_category': int(req['category'] == 2),
        '10_category': int(req['category'] == 10), '15_category': int(req['category'] == 15), '17_category': int(req['category'] == 17), '19_category': int(req['category'] == 19),
        '20_category': int(req['category'] == 20), '22_category': int(req['category'] == 22), '23_category': int(req['category'] == 23), '24_category': int(req['category'] == 24),
        '25_category': int(req['category'] == 25), '26_category': int(req['category'] == 26), '27_category': int(req['category'] == 27), '28_category': int(req['category'] == 28),
        '29_category': int(req['category'] == 29), '43_category': int(req['category'] == 43), 'pub_julian': tt.tm_yday,
        'pub_month': int(req['month']), # 'pub_hour': [1], 'pub_min': [40],
        'duration': int(req['duration'])
    }
    # print(template)

    rows = {
        # 'comments_disabled': [],
        # 'ratings_disabled': [],
        '2_category': [],
        '10_category': [], '15_category': [], '17_category': [], '19_category': [],
        '20_category': [], '22_category': [], '23_category': [], '24_category': [],
        '25_category': [], '26_category': [], '27_category': [], '28_category': [],
        '29_category': [], '43_category': [], 'pub_julian': [],
        'pub_month': [], 'pub_hour': [], 'pub_min': [], 'duration': []
    }

    for h in range(0, 24):
        for m in range(0, 60):
            rows['pub_hour'].append(h)
            rows['pub_min'].append(m)
            for k in template.keys():
                rows[k].append(template[k])

    return pd.DataFrame(rows)

def predict_batch(model, scaler, X_test):
    rescaled_X_test = scaler.transform(X_test)
    predictions = model.predict(rescaled_X_test)
    return predictions
