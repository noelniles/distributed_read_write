import datetime, os, sys


class logger:
    def __init__(self, pc):
        self.now = datetime.datetime.now()
        self.fn = '{}.log'.format(pc.id)
        self.logdir = 'logs'
        self.logpath = os.path.join(self.logdir, self.fn)

        if not os.path.exists(self.logdir):
            os.makedirs(os.path.join('./', self.logdir))

        with open(self.logpath, 'a') as f:
            f.write('{} {}\n'.format("started at: ", self.now))


