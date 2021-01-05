# Project Euler
# Problem 10: Summation of Primes

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
    n = next(prime)
    sum_primes = 0

    while n < 2_000_000:
        sum_primes += n
        n = next(prime)
    print(f"Sum of primes is {sum_primes}")
