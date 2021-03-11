# Project Euler
# Problem 52: Permuted Multiples

def solve(num):
    n = 1
    found = False
    while not found:
        curr = set(str(n))
        for i in range(2, num + 1):
            if curr != set(str(n*i)):
                break
            if i == num and curr == set(str(n*i)):
                print(n)
                found = True
                break
        n += 1


if __name__=="__main__":
    solve(6)