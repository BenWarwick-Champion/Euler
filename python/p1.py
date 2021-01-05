# Project Euler
# Problem 1: Multiples of 3 and 5

answer = sum([num for num in range(1000) if (num % 3 == 0) or (num % 5 == 0)])
print("Problem 1 solution is:", answer)