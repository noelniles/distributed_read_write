#!/usr/bin/env python3
"""
A driver for PC simulation

Right now this just starts one client and reads from stdin.
"""
import random, socket, sys
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

        # This is used to randomly choose reading or writing actions.
        self.actions = [self.write_randomly, self.read_randomly]

        while 1:
            # read from keyboard
            line = sys.stdin.readline()
            if line == '\n':
                break
            self.sock.send(line.encode('utf-8'))
            print(self.sock.recv(self.size))
            self.behave_randomly()
        self.sock.close()

    def behave_randomly(self):
        """Randomly choose read or write."""
        ind = random.randint(0,1)
        choice = self.actions[ind]

        # Call the random function. Could be read or write.
        choice()

    def read_randomly(self):
        """Read the shared file."""
        print('Reading')

    def write_randomly(self):
        """Generate a random number [1-3] and act accordingly.

            1. PC does not want access to file send message:"OK WRITE".
            2. PC wants access but is later than others so delay message.
            3. PC wants access and is earliest so send message:"WRITE".
        """
        choice = random.randint(1,3)
        if choice == 1:
            print('choice is one')
            self.sock.send('OK WRITING'.encode('utf-8'))
            print(self.sock.recv(self.size))
        if choice == 2:
            print('I will wait until the other guy is done.')
        if choice == 3:
            print('You should wait until I am done writing')

if __name__ == '__main__':
    """Run this from the command line to generate a new PC."""
    pc = PC()
