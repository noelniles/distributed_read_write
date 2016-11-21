import logger, vector_clock


class pc:
    def __init__(self, pcid, npcs):
        self.id = pcid
        self.logger = logger(self)
        self.clock = vector_clock(npcs)

