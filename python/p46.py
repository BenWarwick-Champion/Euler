# Project Euler
# Problem 46: Goldbach's Other Conjecture

from math import sqrt, ceil

from utils.utils import create_prime_array

def check_goldbach(num, prime_array):
    for prime in prime_array:
        if prime >= num:
            return False
        for x in range(ceil(sqrt(num))):
            if prime + (2*(x**2)) == num:
                return True
    print("Something went wrong?")
    return False

def main():
    prime_array = create_prime_array(1_000_000)
    primes = set(prime_array)

    n = 2
    found = False
    while not found:
        n += 1
        if n % 2 == 0 or n in primes:
            continue

        if not check_goldbach(n, prime_array):
            found = True

    print(f"Smallest odd composite is {n}")

if __name__=="__main__":
    main()