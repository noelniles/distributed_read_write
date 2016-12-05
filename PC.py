#!/usr/bin/env python3
"""
A driver for PC simulation

Right now this just starts one client and reads from stdin.
"""
import random, socket, sys, time
from logger import logger


class PC:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5015
        self.size = 1024

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

        self.vclock = [0]*10
        self.id = self.sock.fileno()      # It's unique, small, a good index.
        print('id: ', self.id)

        self.sockname = self.sock.getsockname()[-1]
        self.l = logger(self.sockname)

        # List of functions that we can choose randomly from.
        self.actions = [self.write_randomly, self.read_randomly]

        # TODO: I think we should just remove the while loop and just let each
        # client run wild randomly requesting reads and writes and just see 
        # what happens with our half-assed vector clock.
        while 1:
            self.behave_randomly()
        self.sock.close()

    def behave_randomly(self):
        """Randomly choose read or write."""
        self.sock.sendall(bytes(self.vclock))
        ind = random.randint(0,1)
        choice = self.actions[ind]

        # Call the random function. Could be read or write.
        print('Chose: ', choice.__name__)
        choice()
        time.sleep(1)

    def read_randomly(self):
        """Read the shared file."""
        self.update_clock()
        print('Reading')
        print('vclock: ', self.vclock)

    def write_randomly(self):
        """Generate a random number [1-3] and act accordingly.

            1. PC does not want access to file send message:"OK WRITE".
            2. PC wants access but is later than others so delay message.
            3. PC wants access and is earliest so send message:"WRITE".
        """
        self.update_clock()
        print('vclock: ', self.vclock)
        choice = random.randint(1,3)
        if choice == 1:
            print('I do not need access to the file.')
            self.sock.send('WRITING OK'.encode('utf-8'))
            print(self.sock.recv(self.size))
        if choice == 2:
            print('I will wait until the other guy is done.')
            self.sock.send('WRITING OK'.encode('utf-8'))
            print(self.sock.recv(self.size))
        if choice == 3:
            print('You should wait until I am done writing')

    def write_to_shared_file(self):
        """Write some stuff to the shared file"""
        pass

    def update_clock(self):
        self.vclock[self.id] = self.vclock[self.id] + 1

if __name__ == '__main__':
    """Run this from the command line to generate a new PC."""
    pc = PC()
