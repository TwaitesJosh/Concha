from model import Model
from joblib import load
import numpy as np
import pandas as pd

clf = Model()
model_path = 'lib/model/csv_for_model_3_input.csv'
with open(model_path, 'rb') as f:
    clf.model_from_csv(f)

inp = input("Type model input, as X, X, X\n")
fmt_in = np.array(inp.split(','), dtype=np.int)
fmt_in = pd.DataFrame(fmt_in.reshape(1, -1), columns=['2k', '4k', '6k'])
print(clf.predict(fmt_in))
