# Project Euler
# Problem 27: Quadratic Primes

from utils.utils import create_prime_array

if __name__ == "__main__":
    prime_array = create_prime_array(1_000_000)
    prime_set = set(prime_array)
    answer, coeffs = 0, (0, 0)
    max_count = 0
    for prime1 in prime_array:
        if prime1 > 1000:
            break
        for prime2 in prime_array:
            if prime2 > 1000:
                break
            count, n = 0, 0
            result = n**2 + (-prime1*n) + prime2
            while result in prime_set:
                count += 1
                n += 1
                result = n**2 + (-prime1*n) + prime2
            if count > max_count:
                max_count = count
                coeffs = (-prime1, prime2)
                answer = -prime1 * prime2
    
    print(f"Product of the coefficients {coeffs} is {answer}.")