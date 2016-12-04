#!/usr/bin/env python3
import select, socket, sys, threading
from Client import Client


class Server:
    def __init__(self):
        self.host = ''
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        """Tries to open a socket."""
        try:
            self.server = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)
            print("self.server...", self.server)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except(socket.error, (value, message)):
            if self.server:
                self.server.close()
            print("Could not open socket: ", message)
            sys.exit(1)

    def run(self):
        self.open_socket()
        input = [self.server, sys.stdin]
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(input, [], [])
            for s in inputready:
                print(s)
                if s == self.server:
                    client, address = self.server.accept()
                    c = Client(client, address)
                    c.start()
                    self.threads.append(c)
                    print(self.threads)
                elif s == sys.stdin:
                    junk = sys.stdin.readline()
                    running = 0

        self.server.close()
        for c in self.threads:
            c.join()

if __name__ == '__main__':
    s = Server()
    s.run()
