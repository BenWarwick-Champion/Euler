# Project Euler
# Problem 49: Prime Permutations

from itertools import permutations

from utils.utils import create_prime_array

def find_perms(primes, p_set):
    for prime in primes:
        for n in permutations(str(prime)):
            perm = int(''.join(n))
            if perm == 1487 or perm == 4817 or perm == 8147:
                continue
            if perm != prime and perm in p_set:
                diff = perm - prime
                p3 = perm + diff
                if p3 in p_set:
                    for p in permutations(str(prime)):
                        perm2 = int(''.join(p))
                        if p3 == perm2:
                            return prime, diff

def solve():
    p_array = create_prime_array(10_000)
    p = 0
    while p_array[p] < 1000:
        p += 1

    primes = p_array[p:]
    p_set = set(primes)

    start, diff = find_perms(primes, p_set)
    print(start, start+diff, start+diff+diff)

if __name__=="__main__":
    solve()