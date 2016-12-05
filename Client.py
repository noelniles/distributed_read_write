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
            app anyway.

            This means that the client can use any attributes of the server.
        """
        threading.Thread.__init__(self)
        self.client = server.client         # socket object
        self.address = server.address
        self.size = 1024                    # make read/write size
        self.id = self.client.fileno()      # It's unique, small, a good index.
        self.nneighbors = server.nclients   # Not a typo. The number of clients
        self.server = server                # And the kitchen sink...

    def run(self):
        """This method actually overrides the threading run method so that we
           can just call Client.start() and it calls this method.
        """
        running = 1
        while running:
            data = self.client.recv(self.size) # received bytes object
            print(data)

            if data:
                self.client.send(data)
            else:
                self.client.close()
                running = 0


if __name__ == '__main__':
    print("This should be imported not run directly.")
    sys.exit(2)
