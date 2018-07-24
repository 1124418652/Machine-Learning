#-*- coding: utf-8 -*-
import numpy as np 
import copy

class Perceptron(object):
	def __init__(self, data):
		self.__data = data

	def segmentation(self):
		label = []
		input_array = copy.deepcopy(self.__data)
		for line in input_array:
			label.append(line.pop())
		return input_array, label

	def norm_perceptron(self, speed=1):
		input_array, label = self.segmentation()
		input_array = np.array(input_array)
		w = np.zeros(len(input_array[0]))
		b = 0

		error_list = set()
		for index, value in enumerate(input_array):
			if(((value*w).sum()+b)*label[index]<=0):
				error_list.add(index)

		num = 0

		while(error_list):
			for index, value in enumerate(input_array):
				num = num + 1
				if(((value*w).sum()+b)*label[index]<=0):
					error_list.add(index)
					w = w + speed*value*label[index]
					b = b + speed*label[index]
					break
		
				elif(((value*w).sum()+b)*label[index]>0 and index in error_list):
					error_list.remove(index)

		print("The frequency of training: %d" %(num))
		print("The final model: %s*x1 + %s*x2 + %s" %(w[0], w[1], b))				
						
						

def main():
	data = [[3, 3, 1],
			[4, 3, 1],
			[1, 1, -1],
			[0, 2, -1]]
	percept = Perceptron(data)
	percept.norm_perceptron()


if __name__ == '__main__':
	main()