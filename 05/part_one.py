#!/usr/bin/env python3

import sys

def polymer_reaction(polymer):
    reacted_polymer = list(polymer)
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


if __name__ == "__main__":
    polymer = sys.stdin.read().split()[0]
    result = polymer_reaction(polymer)
    print(f"{len(result)}")
