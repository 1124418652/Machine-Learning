# -*- coding: utf-8 -*-
"""
# project: Linear Classify
# author:  xhj
# email:   1124418652@qq.com
# date:    2018 9/24
"""

import os
import csv
import numpy as np

class Linear_classify(object):

    def modify_data(self, path):
        ifopen = open(path, "r")
        ofopen = open("training.txt", "w", newline = "")     # 如果不加 newline = ""，则会写入空行
        reader = csv.reader(ifopen)
        writer = csv.writer(ofopen)

        for i in reader:
            if len(i) != 0:
                # print(i)
                i = i[0].split("\t")
                i = [float(x) for x in i]
                writer.writerow(i)

        ifopen.close()
        ofopen.close()

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

        self.data_set = np.array(data, dtype = "float64")
        self.labels = np.array(label, dtype = "float64")

        return self.data_set, self.labels

def main():
    classify = Linear_classify()
    data, label = classify.load_data("training.txt")
    print(data, label)
