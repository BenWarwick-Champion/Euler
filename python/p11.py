# Project Euler
# Problem 11: Largest product in a grid

#                     (-3,3)
#              (-2,2)
#       (-1,1)
# (0,0) (0, 1) (0, 2) (0, 3)
# (1,0) (1, 1)
# (2,0)        (2, 2)
# (3,0)               (3, 3)

# Finding the max product of the above (with some bounds checking)
# for each element in the grid 

def max_prod(grid, r, c, rng):
    # row product, diag down, diag up, column product
    r_prod, dd_prod, du_prod, c_prod = 1, 1, 1, 1
    for diff in range(rng):
        if r + diff < len(grid):
            r_prod *= int(grid[r+diff][c])
        if r + diff < len(grid) and c + diff < len(grid[0]):
            dd_prod *= int(grid[r+diff][c+diff])
        if 0 <= r - diff < len(grid) and c + diff < len(grid[0]):
            du_prod *= int(grid[r-diff][c+diff])
        if c + diff < len(grid[0]):
            c_prod *= int(grid[r][c+diff])
    return max(r_prod, dd_prod, du_prod, c_prod)
    

if __name__ == "__main__":
    with open("Data/p11.txt", "r") as f:
        data = [line.split() for line in f.readlines()]

    largest_prod = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            prod = max_prod(data, r, c, 4)
            if prod > largest_prod:
                largest_prod = prod

    print(f"Largest 4 digit product is: {largest_prod}")