# Project Euler
# Problem 8: Largest product in series

from math import prod

def kernel_sum(string, k):
    max_sum = 0
    for i in range(k, len(string)):
        res = prod([int(n) for n in string[i-k:i]])
        if res > max_sum:
            max_sum = res
    return max_sum


if __name__ == "__main__":
    with open("Data/p8.txt", "r") as f:
        data = ''.join([line.strip() for line in f.readlines()])

    print(f"Largest product is {kernel_sum(data, 13)}")