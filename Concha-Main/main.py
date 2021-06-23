#!/usr/bin/env python

import numpy as np
import pandas as pd
from model import Model

clf_3 = Model()
model_path_3 = 'csv_for_model_3_input.csv'

with open(model_path_3, 'rb') as f:
    clf_3.model_from_csv(f)


inp = input("Type model input, as 2k, 4k, 6k:\n")
fmt_in = np.array([float(x) for x in inp.split(',')])
fmt_in = pd.DataFrame(fmt_in.reshape(1, -1), columns=['2k', '4k', '6k'])

print('Prediction is: ')
out_3 = clf_3.predict_3(fmt_in)
print(out_3.to_string(index=False))