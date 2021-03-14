# Project Euler
# Problem 55: Lychrel Numbers

def is_palindrome(num: int) -> bool:
    digits = str(num)
    if digits == digits[::-1]:
        return True
    else:
        return False

def is_lychrel(num: int, depth: int) -> bool:
    if depth == 0:
        return True
    
    if is_palindrome(num) and depth < 50:
        return False

    return is_lychrel(num + int(str(num)[::-1]), depth - 1)


def solve():
    print(sum(is_lychrel(n, 50) for n in range(1, 10_000)))        

if __name__=="__main__":
    solve()