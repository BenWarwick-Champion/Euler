# Project Euler
# Problem 4: Largest Palindrome Product

def find_pal():
    for x in range(999, 100, -1):
        for y in range(999, 990, -1):
            res = x * y
            if str(res) == str(res)[::-1]:
                return res
    return "Not found"

if __name__ == "__main__":
    res = find_pal()
    print(f"Largest palindrome from 3 digit numbers is {res}.") # 906609