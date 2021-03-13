# Project Euler
# Problem 53: Combinatoric Selections

from math import factorial

def solve():
    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            result = factorial(n) / (factorial(r) * factorial(n-r))
            if result > 1_000_000:
                count += 1
    print(count)

if __name__=="__main__":
    solve()