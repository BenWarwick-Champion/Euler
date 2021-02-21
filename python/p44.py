# Project Euler
# Problem 44: Pentagon Numbers

from math import sqrt


def pent_number(n):
    return (3*n**2 - n)//2


def gen_pents():
    ind = 1
    while True:
        yield pent_number(ind)
        ind += 1


def is_pent(num):
    ind = (sqrt(24*num + 1) + 1) / 6
    if ind.is_integer():
        return True
    else:
        return False


def main():
    pent = gen_pents()
    pents = []

    found = False
    while not found:
        num = next(pent)
        for p in pents[::-1]:
            if is_pent(num - p) and is_pent(num + p):
                found = True
                print(f"Pents are: {num} and {p}; diff is {num - p}.")
                break
        pents.append(num)


if __name__ == "__main__":
    main()
