# Project Euler
# Problem 17: Number Letter Counts

def count_letters(nums):
    count = 0
    for num in nums:
        for letter in num.casefold():
            if letter.isalpha():
                count += 1
        if 'hundred ' in num.casefold():
            count += 3
    return count
        


if __name__ == "__main__":
    with open("Data/p17.txt", "r") as f:
        data = [line.strip().split(' \t')[1] for line in f.readlines()]

    print(f"There are {count_letters(data)} letters in the numbers 1 to 1000.")