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
sys.path.append(os.path.join(os.path.abspath("."), "../"))
from linear_classify import Linear_classify

class logistic(Linear_classify):
    def __init__(self, alpha = 0.1, iterate = 100):
        self._alpha = alpha
        self._iterate = iterate

    # def modify_data(self, path):
    #     ifopen = open(path, "r")
    #     ofopen = open("training.txt", "w", newline = "")     # 如果不加 newline = ""，则会写入空行
    #     reader = csv.reader(ifopen)
    #     writer = csv.writer(ofopen)

    #     for i in reader:
    #         if len(i) != 0:
    #             # print(i)
    #             i = i[0].split("\t")
    #             i = [float(x) for x in i]
    #             writer.writerow(i)

    #     ifopen.close()
    #     ofopen.close()

    # def load_data(self, path):
    #     if False == os.path.isfile(path):
    #         print("Don't find this file!")
    #         exit()

    #     data = []
    #     label = []
    #     with open(path, "r") as fr:
    #         reader = csv.reader(fr)
    #         for row in reader:
    #             data.append(row[: -1])
    #             label.append(row[-1])

    #     self.data_set = np.array(data, dtype = "float64")
    #     self.labels = np.array(label, dtype = "float64")

    #     return self.data_set, self.labels

    def training(self, data_set, labels):
        """
        Lose Function: -[yi*log(y) + (1-yi)log(1-y)]
        """
        dim = len(data_set[0])
        num = len(labels)
        w = np.zeros(dim, dtype = "float64")
        b = 0.0

        for iter in range(self._iterate):
            z = np.dot(data_set, w)

            for i in range(num):
                a = exp(z[i] + b) / (1 + exp(z[i] + b))
                dw = (a - labels[i]) * data_set[i]
                w -= self._alpha * dw
                b -= self._alpha * (a - labels[i])

        self._w, self._b = w, b
        return self._w, self._b

    def predict(self, data, w, b):
        a = exp(np.dot(data, w) + b) / (1 + exp(np.dot(data, w) + b))
        if a >= 0.5:
            return 1
        else:
            return 0

    def testing(self, data_set, labels):
        error = 0.0
        num = len(labels)
        predict_label = np.zeros(num)

        for i in range(num):
            if self.predict(data_set[i], self._w, self._b) == 1:
                predict_label[i] = 1

        diff = predict_label - labels
        error = np.array([abs(x) for x in diff]).sum() / num
        print("Error of this model: ", error)

        error_point = []
        for i in range(num):
            if 0 != diff[i]:
                error_point.append(data_set[i])

        return error_point

    def show_data(self, data_set, labels):
        num = len(labels)
        pos_data = []
        neg_data = []
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for i in range(num):
            if 1 == labels[i]:
                pos_data.append(data_set[i])
            else:
                neg_data.append(data_set[i])

        # print(len(pos_data) + len(neg_data))
        # print(pos_data)
        pos_data = np.array(pos_data)
        neg_data = np.array(neg_data)
        ax.plot(pos_data[:,0], pos_data[:,1], "b*")
        ax.plot(neg_data[:,0], neg_data[:,1], "ro")
        plt.show()

def main():
    train_path = "training.txt"
    test_path = "testing.txt"
    logis = logistic()
    data, label = logis.load_data("training.txt")
    # logis.show_data(data, label)
    w, b = logis.training(data, label)
    error_point = np.array(logis.testing(data, label))
    # print(w, b)
    # plt.plot(error_point[:,0], error_point[:,1], "*")
    # plt.show()
    # print(exp(np.dot([1,1], w) + b) / (1 + exp(np.dot([1,1], w) + b)))
    # print(logis.predict([-1.395634,4.662541], w, b))

if __name__ == '__main__':
    main()
