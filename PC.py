#!/usr/bin/env python3
"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""
import socket
import sys
from logger import logger


class PC:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5015
        self.size = 1024

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

        self.sockname = self.sock.getsockname()[-1]
        self.l = logger(self.sockname)

        while 1:
            # read from keyboard
            line = sys.stdin.readline()
            if line == '\n':
                break
            self.sock.send(line.encode('utf-8'))
        self.sock.close()


if __name__ == '__main__':
    pc = PC()
