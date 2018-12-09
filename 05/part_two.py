#!/usr/bin/env python3

import sys

def polymer_reaction(polymer, without):
    reacted_polymer = list(filter(lambda c: c != without.lower() and c != without.upper(), polymer))
    reacted = True
    while reacted:
        reacted = False
        
        # using arrays as stacks
        polymer = list(reversed(reacted_polymer))
        reacted_polymer = [polymer.pop()]

        while polymer:
            left = reacted_polymer[-1]
            right = polymer[-1]

            if abs(ord(left) - ord(right)) == 32:
                reacted = True

                reacted_polymer.pop()
                polymer.pop()

                if not reacted_polymer and polymer:
                   reacted_polymer.append(polymer.pop())
            else:
               reacted_polymer.append(polymer.pop())

    return ''.join(reacted_polymer) 


def find_shortest(polymer):
    available_chars = set([c.lower() for c in polymer])
    polymers = [polymer_reaction(polymer, c) for c in available_chars]
    available_results = {polymer: len(polymer) for polymer in polymers}

    return min(available_results, key=available_results.get)
        

if __name__ == "__main__":
    polymer = sys.stdin.read().split()[0]
    result = find_shortest(polymer)
    print(f"{len(result)}")
