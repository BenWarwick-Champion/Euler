# Projet Euler
# Problem 23: Non-abundant Sums

from utils.utils import find_divisors

if __name__ == "__main__":
    abundants = []
    for num in range(1, 28123):
        if sum(find_divisors(num)) > num:
            abundants.append(num)

    ab_sums = set([x+y for x in abundants for y in abundants])
    numbers = set(range(1, 28123))

    answer = numbers.difference(ab_sums)
    print("Sum of all positive ints that aren't the sum of two abundant numbers:", sum(answer))