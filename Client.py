#!/usr/bin/env python3
import select, socket, sys, threading


class Client(threading.Thread):
    def __init__(self, server):
        """Initialize a new client.

            client:     a new socket object
            address:    the address that bound to the socket on the other end

            The Client is initialized with a server because I kept having to 
            add more parameters to the constructor and it was just a pain in 
            the ass. The client server paradigm is kind of tenuous in this
            app anyway. Enjoy!
        """
        threading.Thread.__init__(self)
        self.client = server.client
        self.address = server.address
        self.size = 1024
        self.vclock = server.vclock
        self.id = self.client.fileno()
        self.nneighbors = server.nclients   # Not a typo. The number of clients

    def run(self):
        """This method actually overrides the threading run method so that we
           can just call Client.start() and it calls this method.
        """
        running = 1
        while running:
            # a bytes object representing the data received
            data = self.client.recv(self.size)
            self.vclock[self.id] = self.vclock[self.client.fileno()] + 1

            if data:
                # send the data to the socket returns the number of bytes sent
                self.can_write()
                self.client.send(data)
            else:
                # mark the socket closed
                self.client.close()
                running = 0

    def can_write(self):
        if self.vclock[self.id] == max(self.vclock):
            print('OK WRITE')


if __name__ == '__main__':
    # This should be imported not run directly.
    pass
