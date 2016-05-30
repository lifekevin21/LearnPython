# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def dels(x):
    if x == 1:
        return True
        
    divid = filter(lambda i: x % i == 0, range(2, x-1))
    return not len(divid) == 0
    
    
print filter(dels, range(1, 101))