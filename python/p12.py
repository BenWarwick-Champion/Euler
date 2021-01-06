# Project Euler
# Problem 12: Highly Divisible Triangular Number

from math import sqrt, ceil

def next_triangle():
    n, tri_num = 0, 0
    while True:
        n += 1
        tri_num += n
        yield tri_num

def count_divisors(num):
    # Maybe Less Naive Again?
    count = 0
    if num % sqrt(num) == 0:
        count += 1
    for n in range(1, ceil(sqrt(num))):
        if num % n == 0:
            count += 2

    # # Less Naive Solution - Struggles after 4_000_000
    # if num % 2 == 0:
    #     for n in range(1, num//2 + 1):
    #         if num % n == 0:
    #             count += 1
    # else:
    #     for n in range(1, num//3 + 1, 2):
    #         if num % n == 0: 
    #             count += 1

    # # Most Naive Solution - Struggles after 1_000_000
    # for n in range(1, num):
    #     if num % n == 0:
    #         count += 1

    return count

if __name__ == "__main__":
    tri = next_triangle()

    num = next(tri)
    while count_divisors(num) < 500:
        num = next(tri)
    print(f"The first triangle number with more than 500 divisors is {num}")
