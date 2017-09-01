# -*- coding: utf-8 -*-

import numpy as np
import operator

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
    inx = np.array([1,0.9])
    dataSet = np.array([[1,1.1],[1,1],[0,0],[0,0.1]])
    labels = ['a','a','b','b']
    print(classify(inx, dataSet, labels, 1))
