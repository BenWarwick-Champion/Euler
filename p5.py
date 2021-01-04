# Project Euler
# Problem 5: Smallest Multiple

def check_multiples(num):
    for i in range(1, 20):
        if num % i != 0:
            return False
    return True

if __name__ == "__main__":
    # Naive solution only using 20*3 to filter checked numbers
    number = 60
    while check_multiples(number) == False:
        number += 60
    print(f"The smallest multiple of 1-20 is {number}.") # 232792560
