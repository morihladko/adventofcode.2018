#!/usr/bin/env python3

import sys
from collections import Counter 

def find_id(input_file):
    words = input_file.readlines()
    length = len(words[0])

    for i in range(length):
        c = Counter(w[0:i] + w[i+1:length] for w in words)

        for word, count in c.items():
            if count > 1:
                print(f"Word {word} is counted {count}")
    
            

if __name__ == "__main__":
    find_id(sys.stdin)

#    print(f"ID: {ajdi}")
