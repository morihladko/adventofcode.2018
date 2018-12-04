#!/usr/bin/env python3

import sys
from collections import defaultdict


def count_letters(word):
    counter = defaultdict(int)
    twos = 0
    threes = 0

    for c in word:
        counter[c] += 1

    for counts in counter.values():
        if counts == 2:
            twos = 1

        if counts == 3:
            threes = 1

    return twos, threes

def find_checksum(input_file):
    c_2 = 0
    c_3 = 0

    for line in input_file:
        twos, threes = count_letters(line)

        c_2 += twos
        c_3 += threes

    return c_2 * c_3
            

if __name__ == "__main__":
    checksum = find_checksum(sys.stdin)

    print(f"Checksum: {checksum}")
