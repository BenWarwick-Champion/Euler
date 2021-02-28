# Project Euler
# Problem 47: Distinct Prime Factors

def create_prime_array(up_to_num):
    sieve = [True] * (up_to_num + 1)
    prime_array = []
    for n in range(2, up_to_num + 1):
        if sieve[n]:
            prime_array.append(n)
            for i in range(n, up_to_num + 1, n):
                sieve[i] = False
    return prime_array

def prime_factors(num, prime_array):
    """ Finds the prime factors of a number
    Divides by 2 until the result is not an int
    then undoes the last operation and divides by
    the next prime (3) etc. Until the result is
    prime itself.
    """
    factors = []
    result = float(num)
    for prime in prime_array:
        if result.is_integer() and int(result) in prime_array:
            factors.append(int(result))
            break
        if not (result/prime).is_integer():
            continue

        while (result/prime).is_integer():
            factors.append(prime)
            result /= prime

    return factors


def test_prime_factors():
    prime_array = create_prime_array(150_000)
    factors = prime_factors(228, prime_array)
    assert factors == [2, 2, 3, 19], "228 should be [2, 2, 3, 19]"

    factors = prime_factors(189, prime_array)
    assert factors == [3, 3, 3, 7], "189 should be [3, 3, 3, 7]"

    factors = prime_factors(300, prime_array)
    assert factors == [2, 2, 3, 5, 5], "300 should be [2, 2, 3, 5, 5]"

    print("Tests passed")

def main():
    prime_array = create_prime_array(100_000)
    streak = 0
    n = 210
    while True:
        n += 1
        if len(set(prime_factors(n, prime_array))) == 4:
            streak += 1
            if streak > 1:
                print(streak, n)
            if streak == 4:
                print(f"Consecutive 4 are {n-3, n-2, n-1, n}")
                # Expected: 134043
                break
        else:
            streak = 0


if __name__=="__main__":
    main()