# Project Euler
# Problem 3: Largest Prime Factor

def next_prime():
    prime = 1
    while True:
        is_prime = True
        for i in range(2, prime):
            if i != prime and prime % i == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 1

if __name__ == "__main__":
    prime = next_prime()
    curr = next(prime)
    num = 600851475143
    result = num
    factors = []

    while curr < result:
        if result % curr == 0:
            result = result // curr
            factors.append(curr)
        curr = next(prime)
    factors.append(curr)

    print(f"The largest prime factor of {num} is {max(factors)}.")