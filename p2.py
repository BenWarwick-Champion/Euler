# Project Euler
# Problem 2: Even Fibonacci Numbers

def fib(num):
    a, b = 1, 2
    yield a
    yield b
    while a+b < num:
        yield a+b
        a, b = b, a+b

if __name__ == "__main__":
    print("Sum of all even fibonacci numbers under 4,000,000:",
     sum([num for num in fib(4_000_000) if num % 2 == 0]))