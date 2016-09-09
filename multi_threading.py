# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:18:16 2016

@author: kevin
"""

import time, threading


# new thread running
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is end.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s is ended.' % threading.current_thread().name)