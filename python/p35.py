# Project Euler
# Problem 35: Circular Primes

from utils.utils import create_prime_array

def rotate(num):
    l = list(str(num))
    l.append(l.pop(0))
    return  int(''.join(l))


def is_circular_prime(n, primes, circular):
    num = n
    for i in range(len(str(n))+1):
        num = rotate(num)
        if num not in primes:
            return False
    circular.add(num)
    return True

if __name__=="__main__":
    primes = set(create_prime_array(1_000_000))
    circular = set()

    for i in primes:
        is_circular_prime(i, primes, circular)
    print(len(circular))