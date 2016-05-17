# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:35:44 2016

@author: kevin
"""

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)