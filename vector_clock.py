class vector_clock:
    def __init__(self, n):
        self.clock = [0]*n

    def get_clock(self, n):
        return self.clock[n]

    def set_clock(self, sender, recvr):
        pass


if __name__ == '__main__':
    vc = vector_clock(5)
    print(vc.clock)
