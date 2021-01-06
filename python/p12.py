# Project Euler
# Problem 12: Highly Divisible Triangular Number

from time import perf_counter
from math import sqrt, ceil

def next_triangle():
    n, tri_num = 0, 0
    while True:
        n += 1
        tri_num += n
        yield tri_num

def create_prime_array(up_to_num):
    sieve = [True] * (up_to_num + 1)
    prime_array = []
    for prime in range(2, up_to_num + 1):
        if sieve[prime]:
            prime_array.append(prime)
            for i in range(prime, up_to_num + 1, prime):
                sieve[i] = False
    return prime_array

def count_divisors(num):
    # Initial solution with some optimisations
    count = 0
    if num % sqrt(num) == 0:
        count += 1
    for n in range(1, ceil(sqrt(num))):
        if num % n == 0:
            count += 2
    return count

def count_divisors_fast(num):
    count = 1
    for prime in prime_array:
        if prime**2 > num:
            count *= 2
            break
        exp = 1
        while num % prime == 0:
            exp += 1
            num = num // prime
        if exp > 1:
            count *= exp
        if num == 1:
            break
    return count


if __name__ == "__main__":
    tri = next_triangle()
    tri2 = next_triangle()
    # prime_array = create_prime_array(100000)

    start1 = perf_counter()
    prime_array = create_prime_array(100000)
    num = next(tri)
    while count_divisors_fast(num) < 500:
        num = next(tri)
    print(f"The first triangle number with more than 500 divisors is {num}")
    end1 = perf_counter()

    start2 = perf_counter()
    num = next(tri2)
    while count_divisors(num) < 500:
        num = next(tri2)
    print(f"The first triangle number with more than 500 divisors is {num}")
    end2 = perf_counter()

    time1 = end1 - start1
    time2 = end2 - start2
    print(f"Optimised version took: {time1}")
    print(f"Original version took:  {time2}")
