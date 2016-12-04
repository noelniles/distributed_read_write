#!/usr/bin/env python3
import select, socket, sys, threading


class Client(threading.Thread):
    def __init__(self, client, address):
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
            data = self.client.recv(self.size)
            if data:
                self.client.send(data)
            else:
                self.client.close()
                running = 0
