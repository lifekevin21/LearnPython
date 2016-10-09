# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:22:37 2016

@author: kevin
"""

import threading


local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target = process_thread, args = ('Alice', ), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob', ), name= 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()