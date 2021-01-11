import sys
import os

sys.path.append(os.path.abspath("/Euler/python/p18"))
from p18 import max_path_sum

if __name__ == "__main__":
    with open("Data/p67.txt", "r") as f:
        data = [[int(n) for n in line.strip().split()] for line in f.readlines()]

    print("The maximum path sum is:", max_path_sum(data))