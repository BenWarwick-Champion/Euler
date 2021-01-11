# Project Euler
# Utility Functions

from math import sqrt, ceil

def create_prime_array(up_to_num):
    sieve = [True] * (up_to_num + 1)
    prime_array = []
    for prime in range(2, up_to_num + 1):
        if sieve[prime]:
            prime_array.append(prime)
            for i in range(prime, up_to_num + 1, prime):
                sieve[i] = False
    return prime_array

def gen_triangle_nums():
    """Infinitely generate triangle numbers"""
    n, tri_num = 0, 0
    while True:
        n += 1
        tri_num += n
        yield tri_num

def gen_fib():
    """Infinitely generate fibonacci numbers"""
    a, b = 1, 2
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b

def count_divisors(num, prime_array):
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

def find_divisors(num):
    """Returns an unsorted list of divisors"""
    divisors = []
    root = sqrt(num)
    if num % root == 0:
        divisors.append(int(root))
    for n in range(1, ceil(root)):
        if num % n == 0:
            divisors.append(n)
            if n != 1:
                divisors.append(num // n)
    return divisors
    
