# Project Euler
# Problem 30: Digit fifth powers

def is_sum_of_power_digits(n):
    return True if sum([int(digit)**5 for digit in str(n)]) == n else False

if __name__ == "__main__":
    power_numbers = []
    for num in range(2, (9**5)*6):
        if is_sum_of_power_digits(num):
            power_numbers.append(num)
    print(sum(power_numbers))
