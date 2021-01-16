# Project Euler
# Problem 26: Reciprocal Cycles

import itertools

def find_cycle(d):
    seen = {}
    n = 1
    for i in itertools.count():
        if n in seen:
            return i - seen[n]
        else:
            seen[n] = i
            n = n * 10 % d

if __name__ == "__main__":
    max_cycle, answer = 0, 0
    for d in range(1, 1000):
        cycle = find_cycle(d)
        if cycle is not None and cycle > max_cycle:
            max_cycle = cycle
            answer = d
    print("Max cycle is when d =", answer)
