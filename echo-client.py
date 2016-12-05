#!/usr/bin/env python3

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
# import logger, vector_clock, pc
from logger import logger
from vector_clock import vector_clock
from pc import pc
host = 'localhost'
port = 5005
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
sys.stdout.write('%')
print(s.getsockname()[-1])
p = pc(s.getsockname()[-1], 5)
l = logger(p)
while 1:
    # read from keyboard
    line = sys.stdin.readline()
    if line == '\n':
        break
    s.send(line.encode('utf-8'))
    data = s.recv(size)
    sys.stdout.write(str(data))
    sys.stdout.write('%')
    print('*',p.id,'*')
    l.lwrite(line)
s.close()
