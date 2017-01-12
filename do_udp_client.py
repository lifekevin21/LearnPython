# -*- encode:utf-8 -*-


import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Kevin', b'Leona', b'Sam']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

s.close()