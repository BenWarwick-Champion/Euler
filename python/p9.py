# Project Euler
# Problem 9: Special Pythagorean Triplet

from math import sqrt

if __name__ == "__main__":
    num, prod = 1000, 0
    for a in range(num // 3):
        if prod != 0:
            break
        for b in range(num // 2):
            c = sqrt(a**2 + b**2)
            if c.is_integer() and (a + b + c) == num:
                prod = int(a * b * c)
                break
    print(f"Product of abc is {prod}.")