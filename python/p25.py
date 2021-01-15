# Project Euler
# Problem 25: 1000-digit Fibonacci Number

from utils.utils import gen_fib

if __name__ == "__main__":
    fib = gen_fib()
    num, count = 1, 1
    while len(str(num)) < 1000:
        count += 1
        num = next(fib)
    print("The index of the first fib number with over 1000 digits is:", count)