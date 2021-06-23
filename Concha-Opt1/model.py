#!/usr/bin/env python

import numpy as np
import pandas as pd

class Model:

	def __init__(self):
		self.memorised_data = None

	def model_from_csv(self, path):
		self.memorised_data = pd.read_csv(path)

	def predict_3(self, X_test):
		y_pred = X_test.reset_index().merge(self.memorised_data, left_on=['2k', '4k', '6k'],
		                                    right_on=['2k', '4k', '6k'], how='left').sort_index()
		y_pred = y_pred.drop(columns=['index'])
		return y_pred[['500k', '1k', '2k', '3k', '4k', '6k', '8k']]

	def predict_4(self, X_test, optional_variable):
		row = X_test[['2k', '4k', '6k']].reset_index().merge(clf_4.memorised_data,
		                                                     left_on=['2k', '4k', '6k'],
		                                                     right_on=['2k', '4k', '6k'], how='left').sort_index()
		row = row.drop(columns=['index'])
		row = row[row['extra row value'].values == fmt_in[optional_variable].values]
		row.loc[row.index[0],optional_variable] = row.loc[row.index[0],'extra row value']
		return row[['500k', '1k', '2k', '3k', '4k', '6k', '8k']]

	def find_4th_variable(self, X_test):
		return X_test.merge(self.memorised_data, left_on=['2k', '4k', '6k'], right_on=['2k', '4k', '6k'],
		             how='left').iloc[0]['extra row']
					 
