# Project Euler
# Problem 50: Consecutive Prime Sum

def create_prime_array(up_to_num):
    prime_array = []
    sieve = [True] * (up_to_num + 1)
    for n in range(2, up_to_num + 1):
        if sieve[n]:
            prime_array.append(n)
            for i in range(n, up_to_num + 1, n):
                sieve[i] = False
    return prime_array


def solve(limit):
    """ 
    Approach uses two loops.
    Outer starts at 0 increasing to half the length
    of the prime array. (Starting from primes bigger
    than half will only be of streak length 1).
    Inner loop sums primes until the result exceeds
    the limit (1_000_000).
    Longest streaks are stored in a dict (Sum : Streak length)
    """
    primes = create_prime_array(limit)
    p_set = set(primes)
    streaks = {}

    for i in range(len(primes)//2):
        result = 0
        n = i
        while result < limit:
            result += primes[n]
            n += 1
            if (result in p_set and
            (result not in streaks or (n - i) > streaks[result])):
                streaks[result] = n - i

    # This bit of magic finds the max value in the dict
    # and returns its key
    max_prime = max(streaks, key=streaks.get)
    print(max_prime, streaks[max_prime]) 

if __name__ == "__main__":
    solve(1_000_000)
