#! /usr/bin/env python3
import sys
import logger, pc, vector_clock


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: sim [number of pcs]')
        sys.exit(2)

    npc = sys.argv[1]

    pc1 = pc.pc(0, 5)       # Initialize PC0 with 5 other PCs
    print(pc1.clock)
