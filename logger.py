import datetime, os, sys


class logger:
    def __init__(self, pc):
        self.now = datetime.datetime.now()
        self.fn = pc.id + ".log"
        self.logdir = 'logs'
        self.logpath = os.path.join(self.logdir, self.fn)

        if not os.path.exists(self.logdir):
            os.mkdirs(os.path.join('./', logdir))

        with open(self.logpath, 'a') as f:
            f.write('{} {}\n'.format("started at: ", self.now)




