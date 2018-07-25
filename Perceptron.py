#-*- coding: utf-8 -*-
import numpy as np 
import copy
import time

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

	# General form of perceptron model:
	# 1)Randomly select one point to train the model.
	# 2)The grad of parameter w: speed * xi * yi
	# 3)The grad of parameter b: speed * yi     
	
		print("Use normal form of perceptron to train the model")
		start_time = time.time()
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

		end_time = time.time()
		print("Running time of function \"norm_perceptron\": %f s" %(end_time-start_time))
		print("The frequency of training: %d" %(num))
		print("The final model: %s*x1 + %s*x2 + %s\n" %(w[0], w[1], b))				
						
	def dual_perceptron(self, step=1):

	# Dual form of perceptron model:
	# 1)The model: f(x) = sign(sum(aj * yj * xj .* x) + b), 1<=j<=N
	# 2)N is the number of misclassified point
	# 3)aj is the frequency of point j used for modification the model 
	# 4)use gram matrix to storage the value of xj.*x

		print("Use dual perceptron to train the model")
		start_time = time.time()
		input_array, label = self.segmentation()
		input_array = np.array(input_array)
		a = np.zeros(len(input_array))         # array a was used to storage the frequency of point i 
		w = np.zeros(len(input_array[0]))
		b = 0
		num = 0

		gram = np.zeros((len(a), len(a)))      # gram matrix
		for index1, value1 in enumerate(input_array):
			for index2, value2 in enumerate(input_array):
				gram[index1][index2] = (value1*value2).sum()

		error_list = set(range(0, len(label)))

		while(error_list):
			for index, value in enumerate(input_array):
				num += 1
				condition  = ((a*label*gram[index]).sum() + b) * label[index]
				
				if(condition<=0):
					a[index] += 1
					b = b + step*label[index]
					error_list.add(index)

				elif(condition>0 and index in error_list):
					error_list.remove(index)

		for index, value in enumerate(a):
			w += value * input_array[index] * label[index]
		
		end_time = time.time()
		print("Running time of function \"norm_perceptron\": %f s" %(end_time-start_time))
		print("The frequency of training: %d" %(num))
		print("The final model: %s*x1 + %s*x2 + %s\n" %(w[0], w[1], b))	

def main():
	data = [[3, 3, 1],
			[4, 3, 1],
			[1, 1, -1],
			[0, 0, -1],
			[2, 0, -1],
			[0, 2 , -1]]

	percept = Perceptron(data)
	percept.norm_perceptron()
	percept.dual_perceptron()

if __name__ == '__main__':
	main()