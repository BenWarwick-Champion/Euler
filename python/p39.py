# Project Euler
# Problem 39: Integer Right Triangles

from math import sqrt, floor

def find_triangles(perimeter):
    count = 0
    for a in range(1, perimeter//3):
        for b in range(1, perimeter//2):
            c = sqrt(a**2 + b**2)
            if c.is_integer() and a + b + c == perimeter:
                count += 1
    return count

if __name__=="__main__":
    max, ind = 0, 0
    for i in range(1, 1001):
        curr = find_triangles(i)
        if curr > max:
            max = curr
            ind = i

    print(ind)
