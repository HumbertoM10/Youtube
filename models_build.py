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

# import predictions
import data_process

def get_model_scaler(X_train, Y_train):
    scaler = StandardScaler().fit(X_train)
    rescaled_X_train = scaler.transform(X_train)
    model = GradientBoostingRegressor(random_state=21, n_estimators=100)
    model.fit(rescaled_X_train, Y_train)
    return model, scaler

def get_model_dict():
    countries = [
        'US', 'CA', 'DE', 'FR', 'GB'
    ]
    targets = [
        'like_rate', 'dislike_rate',
        'comment_rate', 'time_to_trending',
        'views'
    ]
    models = {}
    for c in countries:
        models[c] = {}
        X, y = data_process.getX_y(c, targets)
        for t in targets:
            y_tar = y[t]
            models[c][t] = get_model_scaler(X, y_tar)

    return models