#!/usr/bin/env python

import numpy as np
import pandas as pd
from model import Model

clf_4 = Model()
model_path_4= 'csv_for_model_4_input.csv'

clf_3 = Model()
model_path_3 = 'csv_for_model_3_input.csv'

with open(model_path_3, 'rb') as f:
    clf_3.model_from_csv(f)

with open(model_path_4, 'rb') as f:
    clf_4.model_from_csv(f)


inp = input("Type model input, as 2k, 4k, 6k:\n")
fmt_in = np.array([float(x) for x in inp.split(',')])
fmt_in = pd.DataFrame(fmt_in.reshape(1, -1), columns=['2k', '4k', '6k'])

optional_variable = clf_4.find_4th_variable(fmt_in)

print('Initial prediction is: ')
out_3 = clf_3.predict_3(fmt_in)
print(out_3.to_string(index=False))
print('Optimal would be with ' + optional_variable)
inp = input('Type model input, as 2k, 4k, 6k, ' + optional_variable + ':\n ')
fmt_in = np.array([int(x) for x in inp.split(',')])
fmt_in = pd.DataFrame(fmt_in.reshape(1, -1), columns=['2k', '4k', '6k', optional_variable])
out_4 = clf_4.predict_4(fmt_in, optional_variable)
print(out_4.to_string(index=False))