# -*- coding: utf-8 -*-
"""
# project: Logistic regression
# author: xhj
# email: 1124418652@qq.com
# date: 2018 9/7
"""

import time
import numpy as np

def seperate_data(data):
    label = []
    x = []

    for line in data:
        x.append(line[:-1])
        label.append(line[-1])

    x = np.array(x)
    return x, label

def model_training(data_set, label, w = None, b = 0):
    """
    logistic model: e^(w*x+b)/[1+e^(w*x+b)]
    cost function:  -[y*log(yi) + (1-y)*log(1-yi)]
    temp variables:
        z = w.T * x
        a = e^z / (1 + e^z)

    """
    pass

def main():
    data = [[3, 3, 1],
            [4, 3, 1],
            [1, 1, -1],
            [0, 0, -1],
            [2, 0, -1],
            [0, 2 , -1]]

if __name__ == '__main__':
    main()
