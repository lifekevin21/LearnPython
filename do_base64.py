# -*- encoding:utf-8 -*-
"""
Create on Tue Jan 10 2017
@Author:Kevin
"""


import base64


def safe_base64_decode(s):
    s = s + b'=' * (4-(len(s)%4))
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

