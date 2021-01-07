# Project Euler
# Large Sum

# This felt like cheating thanks to Pythons native big int support

if __name__ == "__main__":
    with open("Data/p13.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    ans = sum([int(num) for num in data])
    print(f"The first 10 digits of the sum are {str(ans)[:10]}")