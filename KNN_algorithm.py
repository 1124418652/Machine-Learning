# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import operator


def filetodata(filename):
	"""
	the filetodata function is used to extra data from file
	the function has one parameter:
	filename:              the name of the file that contains training data and each line is splited by tab
	"""
	with open(filename, 'r+') as fr:
		dataLines = fr.readlines()
		num_of_lines = len(dataLines)
		returnMat = np.zeros((num_of_lines, 3))
		label_list = []
		index = 0

		for line in dataLines:
			line = line.strip()
			tmp = line.split('\t')
			returnMat[index, :] = tmp[0:3]
			label_list.append(tmp[-1])
			index += 1
		
	return returnMat, label_list


def autoNorm(dataSet):
	"""
	the autoNorm function is used to normalized the data set
	the parameter dataSet should be array type
	this function will return three values:
	normDataSet:             the data set which has been normalized
	ranges:                  a list which contains the ranges of every features
	minVals:                 the min values of every features
	"""
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataSet))
	dataSet_size = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minVals, (dataSet_size, 1))
	normDataSet = normDataSet / np.tile(ranges, (dataSet_size, 1))
	return normDataSet, ranges, minVals
	

def classify(inX, dataSet, labels, k):
    """
    the classify function has four parameters:
    inX:            the input unknow data which should be classify
    dataSet:        the data set which has been classified, each line represents a data point
    labels:         the labels that dataSet contains
    k:              the value of k
    """
    dataSet_size = dataSet.shape[0]
    diff_Mat = np.tile(inX, (dataSet_size, 1)) - dataSet 
    sqdiff_Mat = diff_Mat ** 2
    sqDistance = sqdiff_Mat.sum(axis = 1)
    distance = sqDistance ** 0.5
    sortedDistance = distance.argsort()
    """
    the return value of np.argsort() is a list of subscripts of the sorted distance
    """
    
    classCount = {}
    for i in range(k):
        tmpLable = labels[sortedDistance[i]]
        """
        if there is no key named tmpLable, then the value of tmpLable will be 0
        """ 
        classCount[tmpLable] = classCount.get(tmpLable, 0) + 1

    sortedClassCount = sorted(classCount.iteritems(), key = lambda var: var[1], reverse = True)
    return sortedClassCount[0][0]
    

if __name__ == "__main__":
	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../machinelearninginaction/Ch02/datingTestSet.txt")
	dataSet, labels = filetodata(filename)
	dataSet = autoNorm(dataSet)[0]

	proportion = 0.1
	test_data = dataSet[:int(proportion*len(dataSet)+1)]
	test_labels = labels[:int(proportion*len(labels)+1)]
	error = 0.0
	for i in range(len(test_data)):
		label = classify(test_data[i], dataSet[int(proportion*len(dataSet)+1):], labels[int(proportion*len(labels)+1):], 7)
		if label != test_labels[i]:
			error += 1

	print error
















