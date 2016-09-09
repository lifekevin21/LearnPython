# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:17:34 2016

@author: kevin
"""

from multiprocessing import Process, Queue
import os, time, random


# Writing Data to process
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# Reading Data from process
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # parent process create Queue and pass to all subprocess.
    q = Queue()
    pw = Process(target = write, args = (q, ))
    pr = Process(target = read, args = (q, ))
    # start subprocess and write
    pw.start()
    # start subprocess and read
    pr.start()
    # wait for process pw finish
    pw.join()
    # stop process pr manual
    pr.terminate()