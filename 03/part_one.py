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

    return Position(x=int(x), y=int(y)), Size(width=int(width), height=int(height))
    

def find_overlaps(input_file):
    cloth = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    overlap_counter = 0

    for line in input_file:
        pos, size = parse_line(line)

        for x in range(pos.x, pos.x + size.width):
            for y in range(pos.y, pos.y + size.height):
                cloth[x][y] += 1

                if cloth[x][y] == 2:
                    overlap_counter += 1

    return overlap_counter


if __name__ == "__main__":
    number_of_overlaps = find_overlaps(sys.stdin)
    
    print(f"Number of overlaps: {number_of_overlaps}")
