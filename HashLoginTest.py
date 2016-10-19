# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:21:34 2016

@author: kevin
"""

import hashlib
db={}

def get_md5(passwd):
    md5=hashlib.md5()
    md5.update(passwd.encode('utf-8'))
    return md5.hexdigest()


def login(username,password):
    if db.get(username,None) is not None:
        return db[username]==get_md5(password+username+'*the*Salt*')
    return False

def register(username,password):
    global db
    db[username]=get_md5(password+username+'*the*Salt*')


if __name__ == "__main__":
    register('michael','123456')
    register('bob','888888')
    register('alice','password')

    assert login('michael','123456')
    assert login('bob','888888')
    assert login('alice','password')