#!/usr/bin/python3

'''
export FLASK_APP=server.py
flask run
'''

from flask import Flask, jsonify, make_response, request, render_template, Response
from flask_cors import CORS
import os

import models_build
import predictions
import best_rules

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def root():
    req       = request.json
    res       = {}
    if (req == None): req = request.form

    X = predictions.req_to_rows(req)
    model, scaler = models[req['country']][req['target']]
    Y = predictions.predict_batch(model, scaler, X)
    # print(Y)
    return best_rules.get_best(X, Y, req['target'])
    # bX, bY = best_rules.get_best(X, Y, req['target'])

    # result = ''

    # for index, row in bX.iterrows():
    #     result += str(row['pub_hour']) + ':' + str(row['pub_min']) + '\n'

    # return result

models = models_build.get_model_dict()

app.run(host='0.0.0.0', port= int(os.environ.get('PORT', 5000)))