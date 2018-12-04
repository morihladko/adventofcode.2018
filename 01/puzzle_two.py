#!/usr/bin/env python3

import sys
from collections import defaultdict
from pprint import pprint

def find_frequency(freq, input_file):
    lines = input_file.readlines()
    freqs = defaultdict(int)
    line_i = 0
    line_count = len(lines)

    while True:
        freqs[freq] += 1

        if freqs[freq] == 2:
            return freq

        freq_change = int(lines[line_i])
        freq += int(freq_change)

        line_i = (line_i + 1) % line_count


if __name__ == "__main__":
    freq = find_frequency(0, sys.stdin)

    print(f"Freq: {freq}")
