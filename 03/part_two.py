#!/usr/bin/env python3

from collections import namedtuple
from pprint import pprint
import sys


MAP_SIZE = 1000

Position = namedtuple('Position', ['x', 'y'])
Size = namedtuple('Size', ['height', 'width'])


def parse_line(line):
    cid, _, pos, size = line.split()

    x, y = pos.split(':')[0].split(',')
    width, height = size.split('x')
    cid = int(cid.split('#')[1])

    return cid, Position(x=int(x), y=int(y)), Size(width=int(width), height=int(height))
    

def find_overlaps(input_file):
    cloth = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    overlap_counter = 0
    non_overlapping_claims = set()

    for line in input_file:
        cid, pos, size = parse_line(line)
        non_overlapping_claims.add(cid)

        for x in range(pos.x, pos.x + size.width):
            for y in range(pos.y, pos.y + size.height):
                point = cloth[x][y]

                if point == 0:
                    cloth[x][y] = cid
                else:
                    non_overlapping_claims.discard(cid)
                    non_overlapping_claims.discard(point)

    return list(non_overlapping_claims)

if __name__ == "__main__":
    without_overlaps = find_overlaps(sys.stdin)
    
    print(f"Claims without overlaps: {without_overlaps}")
