# Project Euler
# Problem 43: Sub-string divisibility

from itertools import permutations

def check_property(num, round):
    primes = [2, 3, 5, 7, 11, 13, 17]

    if round == 0 and int(num)%2 == 0:
        return True

    if int(num[-3:]) % primes[round] == 0:
        return check_property(num[:-1], round-1)
    else:
        return False

def main():
    total = 0
    numbers = '0123456789'
    for num in list(permutations(numbers)):
        number = ''.join(num)
        if check_property(number, 6):
            total += int(number)
    print(total)

if __name__=="__main__":
    main()