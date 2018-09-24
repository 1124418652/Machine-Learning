# -*- coding: utf-8 -*-
"""
# project: Logistic regression
# author:  xhj
# email:   1124418652@qq.com
# date:    2018 9/7
"""

import os
import sys
import csv
import time
import numpy as np
from math import exp, log
import matplotlib.pyplot as plt

class logistic(object):
    def __init__(self, alpha = 0.1):
        self._alpha = alpha

    def load_data(self, path):
        if False == os.path.isfile(path):
            print("Don't find this file!")
            exit()

        data = []
        label = []
        with open(path, "r") as fr:
            reader = csv.reader(fr)
            for row in reader:
                data.append(row[: -1])
                label.append(row[-1])

        return np.array(data), np.array(label)

def main():
    path = "train.txt"
    logis = logistic()
    data, label = logis.load_data(path)
    print(data, label)

if __name__ == '__main__':
    main()
