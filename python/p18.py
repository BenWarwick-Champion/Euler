# Project Euler
# Problem 18: Maximum Path Sum I

from operator import add

def max_path_sum(tri):
    while len(tri) > 1:
        last_row = tri[-1]
        next_row = []
        for i in range(len(last_row[:-1])):
            if last_row[i] >= last_row[i+1]:
                next_row.append(last_row[i])
            else:
                next_row.append(last_row[i+1])
        # Performs an element-wise addition of 2 lists
        tri[-2] = list(map(add, tri[-2], next_row))
        tri.pop(-1)
    return tri[0][0]

if __name__ == "__main__":
    with open("Data/p18.txt", "r") as f:
        data = [[int(n) for n in line.strip().split()] for line in f.readlines()]

    print("The maximum path sum is:", max_path_sum(data))