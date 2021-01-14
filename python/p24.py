# Project Euler
# Problem 24: Lexicographic Permutations

from itertools import permutations

if __name__ == "__main__":
    ans = 0
    perm = permutations('0123456789')
    for _ in range(1_000_000):
        ans = next(perm)
    print(f"This: {''.join(ans)}, is the millionth permutation")