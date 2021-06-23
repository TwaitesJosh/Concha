# Serve model as a flask application

#!/usr/bin/env python
import pickle
import numpy as np
import pandas as pd
from model import Model
from flask import Flask, request

model = None
app = Flask(__name__)


def load_model():
    global clf_3
    # model variable refers to the global variable
    clf_3 = Model()
    model_path_3 = 'csv_for_model_3_input.csv'

    with open(model_path_3, 'rb') as f:
        clf_3.model_from_csv(f)

@app.route('/')
def home_endpoint():
    return 'Hello Concha'


@app.route('/predict', methods=['POST'])
def get_prediction():

    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a jso
        data = np.array(data)[np.newaxis,:]
        data = pd.DataFrame(data, columns = ['2k','4k','6k'])        
        data = pd.DataFrame(data, columns=['2k', '4k', '6k'])
        prediction = clf_3.predict_3(data)  # runs globally loaded model on the data
    return prediction.to_string()


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
