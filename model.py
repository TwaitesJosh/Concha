import itertools
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors as NN


def gini_coefficient(x):
	x = x.values
	diffsum = 0
	for i, xi in enumerate(x[:-1], 1):
		diffsum += np.sum(np.abs(xi - x[i:]))
	return diffsum / (len(x) ** 2 * np.mean(x))


class Model:

	def __init__(self):
		self.possible_X_values = np.array(list(itertools.product(5 * np.arange(-1, 21), repeat=3)))
		self.set_of_all_possible_x = set([tuple(x) for x in self.possible_X_values])
		self.group_indexes = None
		self.nn = None
		self.memorised_data = None
		self.x_unique = None

	def model_from_csv(self, path):
		self.memorised_data = pd.read_csv(path)

	def fit(self, X_train, y_train):

		groups = y_train.groupby(['2k', '4k', '6k'])
		self.group_indexes = groups.indices
		set_of_all_X_train = set(self.group_indexes)
		self.x_unique = X_train.groupby(['2k', '4k', '6k']).size().reset_index().rename(columns={0: 'count'})
		self.nn = NN(metric='minkowski', p=3)
		self.nn.fit(self.x_unique[['2k', '4k', '6k']])
		unused_keys = self.set_of_all_possible_x.difference(set_of_all_X_train)

		for k in unused_keys:
			self.group_indexes[k] = []

		self.memorised_data = self.eager_memoisation(y_train)

	def get_Y_train_standard(self, i, y_train):
		ten_n = self.nn.radius_neighbors(i, 50)
		uniq = np.unique((ten_n[0][0]))  # makes use of the fact the unique also sorts that data
		total = 0
		indexes = []
		for i in uniq:
			train_loc = ten_n[1][0][ten_n[0][0] == i]
			total += np.sum(self.x_unique['count'].values[train_loc])
			indexes = np.concatenate((indexes, train_loc))
			if total > 300:
				break
		m = indexes
		l = []
		for j in m:
			l = np.concatenate((self.group_indexes[tuple(self.x_unique.iloc[int(j)].values[:3])], l))
		l = np.array(l, dtype=np.int)

		mode = y_train.iloc[l][['500k', '1k', '3k', '8k']]
		return mode

	def get_Y_lab(self, i, y_train):
		tab = self.get_Y_train_standard(i, y_train)
		return np.round(tab.mean(0) / 5) * 5

	def eager_memoisation(self, y_train):
		y_unique_labs = pd.DataFrame(self.possible_X_values, columns=['2k', '4k', '6k']).apply(
			lambda x: self.get_Y_lab([x], y_train), 1)
		y_unique_labs = pd.DataFrame(y_unique_labs.values.tolist(), index=y_unique_labs.index,
		                             columns=['500k', '1k', '3k', '8k'])
		labeled_x_data = pd.DataFrame(self.possible_X_values, columns=['2k', '4k', '6k']).join(y_unique_labs)
		return labeled_x_data

	def predict(self, X_test):
		y_pred = X_test.reset_index().merge(self.memorised_data, left_on=['2k', '4k', '6k'],
		                                    right_on=['2k', '4k', '6k'], how='left').sort_index()
		y_pred = y_pred.drop(columns=['index'])
		return y_pred[['500k', '1k', '2k', '3k', '4k', '6k', '8k']]

	def find_fourth_variable(self, i):
		tab = self.get_Y_train_standard(i)
		return tab.dropna().apply(gini_coefficient, 0).idxmin()

	def with_fourth_variable(self, y_train, X_train, i, variable, value):
		i[0].append(value)
		groups = y_train.groupby(['2k', '4k', '6k', variable])
		group_indexes = groups.indices

		x_unique = y_train.groupby(['2k', '4k', '6k', variable]).size().reset_index().rename(columns={0: 'count'})
		nn = NN(metric='minkowski', p=3)
		nn.fit(x_unique[['2k', '4k', '6k', variable]])
		ten_n = nn.radius_neighbors(i, 50)
		uniq = np.unique((ten_n[0][0]))  # makes use of the fact the unique also sorts that data
		total = 0
		indexes = []
		for i in uniq:
			train_loc = ten_n[1][0][ten_n[0][0] == i]
			total += np.sum(x_unique['count'].values[train_loc])
			indexes = np.concatenate((indexes, train_loc))
			if total > 300:
				break
		m = indexes
		l = []
		for j in m:
			l = np.concatenate((group_indexes[tuple(x_unique.iloc[int(j)].values[:4])], l))
		l = np.array(l, dtype=np.int)

		mode = y_train.iloc[l][['500k', '1k', '3k', '8k']]
		return np.round(mode.mean(0) / 5) * 5

