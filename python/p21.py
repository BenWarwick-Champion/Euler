# Project Euler
# Problem 21: Amicable Numbers

from utils.utils import find_divisors

def is_amicable(num):
    d_sum = sum(find_divisors(num))
    if sum(find_divisors(d_sum)) == num:
        return num, d_sum
    return 0, 0

if __name__ == "__main__":
    amicable_nums = set()
    for n in range(2, 10_000):
        a, b = is_amicable(n)
        if a != 0 and a != b:
            amicable_nums.add(a)
            amicable_nums.add(b)
    print(sum(amicable_nums))
