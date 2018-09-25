# -*- coding: utf-8 -*-
"""
# project: Perceptron
# author:  xhj
# email:   1124418652@qq.com
# date:    2018 9/24
"""

import os
import sys
import numpy as np
sys.path.append(os.path.join(os.path.abspath("."), "../linear_classify/"))
from linear_classify import Linear_classify

class Perceptron(Linear_classify):
    def training(self, data_set, labels):
        pass

def main():
    percept = Perceptron()
    data, label = percept.load_data("training.txt")
    print(data, label)
