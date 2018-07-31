# -*- coding: utf-8 -*-
"""
# create on 7/30 2018
# author: xhj
# email: 1124418652@qq.com
"""

import time
import copy as cp
import numpy as np
from math import sqrt
from collections import namedtuple
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

		def _segmentation(data):
			input_data = cp.deepcopy(data)
			label = []
			for line in input_data:
				label.append(line.pop())
			return input_data, label

		self.dataSet, self._label = _segmentation(data) 
		self._data_set = np.array(self.dataSet)
		self._k = len(self._data_set[0])

		def create_node(dim, dataSet):

			if not dataSet:
				return None
			dataSet.sort(key=lambda x: x[dim])
			splitPos = len(dataSet)//2
			median = dataSet[splitPos]
			dimNext = (dim+1) % self._k

			return KDNode(median, dim, create_node(dimNext, dataSet[:splitPos]), create_node(dimNext, dataSet[splitPos+1:]))

		self.root = create_node(0, self.dataSet)
		self.result = namedtuple("result_tuple", "nearest_node nearest_dis")     # use a namedtuple to storage the result of tree searching

	def pre_order(self, root):
		print(root.node)
		if(root.childLeft):
			self.pre_order(root.childLeft)
		if(root.childRight):
			self.pre_order(root.childRight)

	def med_order(self, root):
		if(root.childLeft):
			self.med_order(root.childLeft)
		print(root.node)
		if(root.childRight):
			self.med_order(root.childRight)

	def post_order(self, root):
		if(root.childLeft):
			self.post_order(root.childLeft)
		if(root.childRight):
			self.post_order(root.childRight)
		print(root.node)

	def show_data(self):
		if(2 == self._k):
			fig = plt.figure()
			ax = fig.add_subplot(1, 1, 1)
			ax.plot(self._data_set[:,0], self._data_set[:,1], 'o')
			plt.show()

		elif(3 == self.__k):
			fig = plt.figure()
			ax = fig.add_subplot(1,1,1,projection='3d')
			ax.scatter(self._data_set[:,0], self._data_set[:,1], self._data_set[:,2], 'o')
			plt.show()

		else:
			print("The dimention is too high to show in a figure!")

	def search_nearest(self, tree_node, point, nearest_dis):
		"""
		Use recusive, begin with the root node of tree
		dim: the dimention of split current node use
		node: current node
		"""
		if None == tree_node:
			# result("nearest_node nearest_dis")
			return self.result([0]*self._k, float("inf"))       # inf is gigantic

		dim = tree_node.dim 
		node = tree_node.node

		if point[dim] <= node[dim]:
			near_node = tree_node.childLeft                          # 下一个要遍历的节点
			further_node = tree_node.childRight                      # 回退时需要比较的节点
		else:
			near_node = tree_node.childRight
			further_node = tree_node.childLeft

		result1 = self.search_nearest(near_node, point, nearest_dis)      # recusive call the function search_nearest()
		nearest_node = result1.nearest_node                          # 假设当前节点的子节点为距离最近的点
		dist = result1.nearest_dis

		if dist < nearest_dis:                       # nearest_dis为函数传入的参数，用于记录最近的距离
			nearest_dis = dist

		cur_dist = abs(point[dim] - node[dim])       # 测试点与当前节点分割平面的距离
		if nearest_dis < cur_dist:                   # 如果当前最短距离小于测试点与分割平面的距离，则无需遍历分割平面的另一边，直接回退到上一节点
			return self.result(nearest_node, nearest_dis)

		cur_dist = sqrt(sum((a - b) ** 2 for a, b in zip(point, node)))
		if cur_dist < nearest_dis:            # 如果测试点与当前点的距离小于记录的最小距离（nearest_dis），则更新nearest_dis与nearest_node
			nearest_node = node
			nearest_dis = cur_dist

		result2 = self.search_nearest(further_node, point, nearest_dis)
		if result2.nearest_dis < nearest_dis:
			nearest_node = result2.nearest_node
			nearest_dis = result2.nearest_dis

		return self.result(nearest_node, nearest_dis)

def main():
	data = [[2,3,1],[5,4,1],[9,6,1],[4,7,1],[8,1,1],[7,2,1]]
	tree = KDTree(data)
	point = [2,4]
	result = tree.search_nearest(tree.root, point, float("inf"))
	print(result.nearest_node)
	tree.show_data()

if __name__ == '__main__':
	main()
