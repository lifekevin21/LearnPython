# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:51:23 2016

@author: kevin
"""
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        
    
    def __setattr__(self, key, value):
        self[key] = value