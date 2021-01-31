# Project Euler
# Problem 41: Pandigital Prime

from itertools import permutations
from utils.utils import is_prime

def check_for_primes(perms):
    primes = []
    for perm in perms:
        num = int(''.join(perm))
        if is_prime(num):
            primes.append(num)
    return primes

if __name__=="__main__":
    nums = '123456789'
    perms = permutations(nums)
    primes = []
    while len(nums) > 2:
        primes = check_for_primes(perms)
        if len(primes) > 0:
            break
        nums = nums[:-1]
        perms = permutations(nums)
    print("Largest Pandigital Prime is:", max(primes))
