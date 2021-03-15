# Project Euler
# Problem 56: Powerful Digit Sum


def solve():
    max_sum = 0
    for a in range(99, 1, -1):
        for b in range(99, 90, -1):
            num = a ** b
            digits = str(num)
            digit_sum = sum(int(n) for n in digits)
            max_sum = max(max_sum, digit_sum)
    print(max_sum)


if __name__ == "__main__":
    solve()