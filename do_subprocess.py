# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:04:39 2016

@author: kevin
"""



import subprocess

"""
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code', r)
"""

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b'set q = mx \npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit Code:', p.returncode)