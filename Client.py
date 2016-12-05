#!/usr/bin/env python3
import select, socket, sys, threading


class Client(threading.Thread):
    def __init__(self, client, address):
        """Initialize a new client.
            
            client:     a new socket object
            address:    the address that bound to the socket on the other end 
        """
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        """This method actually overrides the threading run method so that we
           can just call Client.start() and it calls this method.
        """
        running = 1
        while running:
            # a bytes object representing the data received
            data = self.client.recv(self.size)
            if data:
                # send the data to the socket returns the number of bytes sent
                print(data)
                self.client.send(data)
            else:
                # mark the socket closed
                self.client.close()
                running = 0

if __name__ == '__main__':
    # This should be imported not run directly.
    pass
