# Project Euler
# Problem 42: Coded Triangle Numbers

from utils.utils import gen_triangle_nums

def calc_value(word):
    total = 0
    for letter in word:
        total += (ord(letter) - 64)
    return total

if __name__=="__main__":
    tri_nums = set()
    tri = gen_triangle_nums()
    for _ in range(1000):
        tri_nums.add(next(tri))

    with open("Data/p42.txt", "r") as f:
        words = f.read().strip('"').split('","')
    
    count = 0
    for word in words:
        if calc_value(word) in tri_nums:
            count += 1
    
    print(f"There are {count} triangle words")