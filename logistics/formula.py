# -*- coding: utf-8 -*-
"""
# project: Logistic regression
# author: xhj
# email: 1124418652@qq.com
# date: 2018 9/20
"""

from sympy import *

z, w, x, b, y, L, yi = symbols("z, w, x, b, y, L, yi")

z = w * x + b
y = exp(z) / (1 + exp(z))
L = -(yi * log(y) + (1 - yi) * log(1 - y))


print(y)
pprint(diff(L, b))
