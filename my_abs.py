# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:40:55 2016

@author: kevin
"""

def my_abs(x):
    if not isinstance(x, int, float):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x