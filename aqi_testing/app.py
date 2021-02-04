from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np
import datetime

app = Flask(__name__)

filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))
cols = ['ds']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    #date = int_features[0].strftime("%Y-%m-%d")
    date_obj = pd.to_datetime(int_features[0])
    final = np.array(date_obj)
    data_unseen = pd.DataFrame(int_features, columns = cols)
    prediction = model.predict(data_unseen)
    prediction = prediction['yhat']
    return render_template('home.html',pred='AQI value is  {}'.format(prediction))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = model.predict(model, data=data_unseen)
    output = prediction['yhat']
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, port = 5000, host = "localhost")
