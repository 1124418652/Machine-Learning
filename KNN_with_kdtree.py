#-*- coding: utf-8 -*-
"""
# create on 2018/7/28
# author: xhj
# email: 1124418652@qq.com
"""

import numpy as np

class KDNode(object):
    def __init__(self, point=None, split=None, left=None, right=None):
        self.point = point
        self.split = split
        self.left = left
        self.right = right

class KDTree(object):
    def __init__(self, data=None):
        self.data = data

    def createTree(self, data):

