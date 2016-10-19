# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:44:42 2016

@author: kevin
"""

import re


s1 = 'someone@gmail.com'
s2 = 'bill.gates@microsoft.com'
pattern = r'^[0-9a-zA-Z\_\.]+@[0-9a-z]+\.[a-z]+$'
re_email = re.compile(pattern)
print('matched: \'%s\'' % re_email.match(s1).group(0))
print('matched: \'%s\'' % re_email.match(s2).group(0))
