# Project Euler
# Problem 34: Digit Factorials

from math import factorial

def is_digit_factorial(num):
    return True if sum([factorial(int(n)) for n in str(num)]) == num else False

if __name__ == "__main__":
    total = 0
    for n in range(10, 100_000):
        if is_digit_factorial(n):
            total += n
    print(total)