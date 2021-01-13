# Project Euler
# Problem 22: Names Scores

def name_to_num(name):
    return sum([(ord(letter) - 64) for letter in name])

if __name__ == "__main__":
    with open("Data/p22.txt", "r") as f:
        names = f.read().strip('"').split('","')
    names.sort()

    total = 0
    for ind, name in enumerate(names):
        total += name_to_num(name) * (ind + 1)

    print("Total of all name scores is:", total)
