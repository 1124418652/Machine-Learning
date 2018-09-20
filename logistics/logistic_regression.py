# -*- coding: utf-8 -*-
"""
# project: Logistic regression
# author: xhj
# email: 1124418652@qq.com
# date: 2018 9/7
"""

import time
import numpy as np
from math import exp, log

def seperate_data(data):
    label = []
    x = []

    for line in data:
        x.append(line[:-1])
        label.append(line[-1])

    x = np.array(x)
    return x, label

def model_training(data_set, label, a = 1, w = None, b = 0, iterate = 400):
    """
    logistic model: e^(w*x+b)/[1+e^(w*x+b)]
    cost function:  -[y*log(yi) + (1-y)*log(1-yi)]
    temp variables:
        z = w.T * x
        a = e^z / (1 + e^z)
    """
    num = len(data_set)
    dims = len(data_set[0])
    # w = np.zeros(dims, float)
    error = 0.0
    i = 0
    w = np.zeros(dims, float)
    b = 0.0

    while(i < iterate):
        index = 0

        for line in data_set:
            z = (w * line).sum() + b
            a = exp(z) / (1+exp(z))
            # error -= (label[index] * log(a) + (1 - label[index]) * log(1 - a))
            w += (label[index] - a) * line
            b += label[index] - a

            index += 1
        i += 1
    return w, b

def main():
    data = [[3, 3, 1],
            [4, 3, 1],
            [1, 1, 0],
            [0, 0, 0],
            [2, 0, 0],
            [0, 2, 0]]
    data = np.array(data)
    x, label = seperate_data(data)
    w, b = model_training(x, label)
    print(w, b)
    print(1 / (1 + exp((w*np.array([0,2])).sum())))

if __name__ == '__main__':
    main()
