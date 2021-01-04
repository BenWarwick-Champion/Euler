# Project Euler
# Problem 6: Sum Square Difference

# Find the difference between the sum of the squares
# of the first 100 natural numbers and the square of
# the sum.

if __name__ == "__main__":
    sum_square = sum(range(1, 101))**2
    squares_sum = sum([n**2 for n in range(1, 101)])
    diff = abs(squares_sum - sum_square)
    print(f"The sum square difference is {diff}.")