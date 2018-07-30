# -*- coding: utf-8 -*-
"""
# create on 7/30 2018
# author: xhj
# email: 1124418652@qq.com
"""

import time
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class KDNode(object):
	def __init__(self, node, dim, childLeft, childRight):
		self.node = node
		self.dim = dim
		self.childLeft = childLeft
		self.childRight = childRight

class KDTree(object):
	def __init__(self, data):

		def __segmentation(data):
			input_data = cp.deepcopy(data)
			label = []
			for line in input_data:
				label.append(line.pop())
			return input_data, label

		self.dataSet, self.__label = __segmentation(data) 
		self.__data_set = np.array(self.dataSet)
		self.__k = len(self.__data_set[0])

		def createNode(dim, dataSet):

			if not dataSet:
				return None
			dataSet.sort(key=lambda x: x[dim])
			splitPos = len(dataSet)//2
			median = dataSet[splitPos]
			dimNext = (dim+1) % self.__k

			return KDNode(median, dim, createNode(dimNext, dataSet[:splitPos]), createNode(dimNext, dataSet[splitPos+1:]))

		self.root = createNode(0, self.dataSet)

	def preOrder(self, root):
		print(root.node)
		if(root.childLeft):
			self.preOrder(root.childLeft)
		if(root.childRight):
			self.preOrder(root.childRight)

	def medOrder(self, root):
		if(root.childLeft):
			self.medOrder(root.childLeft)
		print(root.node)
		if(root.childRight):
			self.medOrder(root.childRight)

	def postOrder(self, root):
		if(root.childLeft):
			self.postOrder(root.childLeft)
		if(root.childRight):
			self.postOrder(root.childRight)
		print(root.node)

	def showData(self):
		if(2 == self.__k):
			fig = plt.figure()
			ax = fig.add_subplot(1, 1, 1)
			ax.plot(self.__data_set[:,0], self.__data_set[:,1], 'o')
			plt.show()

		elif(3 == self.__k):
			fig = plt.figure()
			ax = fig.add_subplot(1,1,1,projection='3d')
			ax.scatter(self.__data_set[:,0], self.__data_set[:,1], self.__data_set[:,2], 'o')
			plt.show()

		else:
			print("The dimention is too high to show in a figure!")

	def 

def main():
	data = [[2,3,1],[5,4,1],[9,6,1],[4,7,1],[8,1,1],[7,2,1]]
	tree = KDTree(data)
	tree.preOrder(tree.root)
	print("\n")
	tree.medOrder(tree.root)
	print("\n")
	tree.postOrder(tree.root)
	tree.showData()

if __name__ == '__main__':
	main()
