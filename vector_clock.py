class vector_clock:
    # def __init__(self, n):
    #     self.clock = [0]*n
    def __init__(self, n):
        self.clock = {}

    def get_clock(self):
        return [(key, val) for key, val in self.items()]
        # return {k:self[k] for k in self}

        # return self.clock

    # def set_clock(self, sender, recvr):
    def set_clock(self, sender, count):
        self.clock[sender] = count

if __name__ == '__main__':
    vc = vector_clock(5)
    print(vc.clock)
