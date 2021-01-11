# Project Euler
# Problem 20: Factorial Digit Sum

from math import factorial

if __name__ == "__main__":

    print(sum([int(n) for n in str(factorial(100))]))