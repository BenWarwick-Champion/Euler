# Project Euler
# Problem 38: Pandigital multiples

def solve():
    for n in range(2, 6):
        for num in range(9876, 1, -1):
            digits = set()
            for i in range(1, n+1):
                digits = digits.union(set(str(num * i)))
            digits.discard('0')
            if len(digits) == 9:
                print(num, n)
                print(f"Largest pandigital: {str(num) + str(num*n)}")
                return

if __name__=="__main__":
    solve()