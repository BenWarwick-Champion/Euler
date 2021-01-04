# Project Euler
# Problem 7: 10,001st Prime

# Makes use of the fact that all primes are odd and
# any n will not have a primefactor greater than sqrt(n)

from math import sqrt, ceil

def next_prime():
    yield 2
    n = 3
    while True:
        is_prime = True
        for i in range(2, ceil(sqrt(n))+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 2

if __name__ == "__main__":
    prime = next_prime()
    for _ in range(10_000):
        next(prime)
    print(next(prime))