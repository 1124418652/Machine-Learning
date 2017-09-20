# -*- coding: utf-8 -*-

import numpy as np
from math import log
import operator


def cal_sannon_ent(dataSet):
	"""
	the function cal_sannon_ent is used to calculate the Shannon entropy of the data set
	"""
	dataSet = np.array(dataSet)
	num_entries = len(dataSet)

	label_count = {}                           #create a dic type to store the appear times of every label
	for label in dataSet[:,-1]:
		if label not in label_count.keys():
			label_count[label] = 1
		else: label_count[label] += 1
		"""
		label_count.get(label,0) += 1
		"""

	Sannon_ent = 0.0
	for key in label_count.keys():
		tmp_ratio = float(label_count[key]) / num_entries
		Sannon_ent -= tmp_ratio * log(tmp_ratio, 2)
	return Sannon_ent


def split_dataSet(dataSet, axis, value):
	"""
	the function split_dataSet is uesd to splite the data set.
	return a child data set doesn't contain the raws whose value of choosing feature is the value want to get
	this function has three parameters:
	dataSet:              the data set that would be splited
	axis:                 the feature which is choosed
	value:                the value of the feature that that you want to get
	"""
	ret_dataSet = []              #ret_dataSet is the data set which contains the rest features
	for featvec in dataSet:
		if featvec[axis] == value:
			"""
			get a data list doesn't contain the feature chosen
			but the raw data of dataSet should not be changed because it would be used many times
			"""
			tmp = featvec[:axis]
			tmp.extend(featvec[axis+1:])
			ret_dataSet.append(tmp)
	return ret_dataSet


def choose_bestFeature_toSplit(dataSet):
	"""
	this function will try to split the data set by given features, calculte the Sannon entropy of every
	spliting way and choose the best way to split the data set
	the difference between the Sannon values of previous node and current node is lagest
	"""
	pre_sannon_value = cal_sannon_ent(dataSet)
	num_axis = len(dataSet[0]) - 1

	best_info_gain = 0.0
	for axis in range(num_axis):
		value = [example[axis] for example in dataSet]
		value = set(value)                                   #the value of every features should not be repeated
		tmp_sannon = 0.0
		for i in value:
			sub_dataSet = split_dataSet(dataSet, axis, i)
			prob = len(sub_dataSet) / float(len(dataSet))
			tmp_sannon += prob * cal_sannon_ent(sub_dataSet)
		infoGain = pre_sannon_value - tmp_sannon
		if best_info_gain < infoGain:
			best_info_gain = infoGain
			best_feature = axis
	return best_feature

		
def majorityCnt(classlist):
	"""
	the parameter of this function is the list of the classes belong to this leaf node
	if the leaf node has more than one classes, this function will return the most class
	as the class of this leaf
	"""
	class_count = {}
	for vote in classlist:
		if vote not in class_count.keys(): class_count[vote] = 1
		class_count[vote] += 1
	
	sorted_class = sorted(class_count.iteritems(), key = operator.itemgetter(1), reverse = True)
	return sorted_class[0][0]


def creat_tree(dataSet, labels):
	"""
	returns a recursive dict representing the dicision tree
	this is a recusive function whose cycle will be exit in three situations:
	1) the leaf node has only one class, then the function will return the value of the class and write it 
		into the dicision tree dictionary, as the classification result using current feature
	2) all features have been used but the leaf node still has more than one classes, then it will invoke 
		function majorityCnt() to find out the most class as the classification using current feature
	3) all of the leaf nodes have been created, then will return the dicision tree
	"""
	class_list = [example[-1] for example in dataSet]
	
	#the leaf node has only one class
	if class_list.count(class_list[0]) == len(class_list):
		return class_list[0]             
	
	#all features have been used
	if len(dataSet[0]) == 1
		return majorityCnt(class_list)
		
	#the node is not a leaf node
	bestFeat = choose_bestFeature_toSplit(dataSet)
	bestFeatLabel = labels(bestFeat)
	











