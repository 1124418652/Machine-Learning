# -*- coding: utf-8 -*-
"""
# project: Perceptron
# author:  xhj
# email:   1124418652@qq.com
# date:    2018 9/24
"""

import os
import sys
import numpy as np
sys.path.append(os.path.join(os.path.abspath("."), ".."))
from linear_classify import Linear_classify

class Perceptron(Linear_classify):
	def change_label(self, labels):
		for i in range(len(labels)):
			if labels[i] == 0:
				labels[i] = -1

		return labels

	def training(self, data_set, labels, model = "normal", step = 0.1):
		if 0 in labels:
			labels = self.change_label(labels)

		w = np.zeros(len(data_set[0]))
		b = 0.0
		num = len(labels)
		error_list = set()

		for index, value in enumerate(data_set):
			if (np.dot(w, value) + b) * labels[index] <= 0:
				error_list.add(index)

		if "normal" == model.lower():
			while(error_list):
				for index, value in enumerate(data_set):
					if (np.dot(w, value) + b) * labels[index] <= 0:
						error_list.add(index)
						w += np.dot(step * labels[index], value)
						b += step * labels[index]
						break
	
					elif (np.dot(w, value) + b) * labels[index] > 0 \
						and index in error_list:
						error_list.remove(index) 
		
		elif "dual" == model.lower():
			a = np.zeros(len(data_set))
		
		return w, b

def main():
	data = [[3, 3],
			[4, 3],
			[1, 1],
			[0, 0],
			[2, 0],
			[0, 2]]
	label = [1,1,-1,-1,-1,-1]
	percept = Perceptron()
	# data, label = percept.load_data("training.txt")
	w, b = percept.training(data, label)
	
	print(w, b)

if __name__ == '__main__':
	main()