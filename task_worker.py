# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:00:41 2016

@author: kevin
"""

# task_worker.py
import time, sys, queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass
	

# 由于这个QueueManager只从网上获取Queue，所以注册时只提供名字
