# Project Euler
# Problem 37: Truncatable Primes

from utils.utils import create_prime_array

def is_trunctable_prime(prime, backwards=False):
    l = list(str(prime))

    while len(l) > 1:
        if backwards:
            l.pop()
        else:
            l.pop(0)
        s = ''.join(l)
        if int(s) in primes:
            continue
        else:
            return False
    return True

if __name__=="__main__":
    primes = set(create_prime_array(1_000_000))
    trunctables = []
    for p in primes:
        if is_trunctable_prime(p) and is_trunctable_prime(p, True):
            trunctables.append(p)
    print(sum(trunctables[4:]))