# Project Euler
# Problem 40: Champernowne's Constant

def create_champernownes(num):
    s = ''
    for i in range(num+1):
        s += str(i)
    return s


if __name__=="__main__":
    f = create_champernownes(25_000)
    ans, i = 1, 1
    while i < 1_000_000:
        ans *= int(f[i])
        i *= 10
    print(ans)
