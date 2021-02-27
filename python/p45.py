# Project Euler
# Problem 45: Triangular, Pentagonal, Hexagonal

# n(n+1)/2
def gen_tri():
    n = 0
    while True:
        n += 1
        yield n * (n+1) // 2

# n(3n-1)/2
def gen_pent():
    n = 0
    while True:
        n += 1
        yield n * ((3*n)-1) // 2

# n(2n-1)
def gen_hex():
    n = 0
    while True:
        n += 1
        yield n * ((2*n)-1)

def main():
    tri, pent, hexa = gen_tri(), gen_pent(), gen_hex()
    tri_num, pent_num, hex_num = 0, 0, 0

    # Surpass the first number
    for _ in range(143):
        tri_num = next(tri)
        pent_num = next(pent)
        hex_num = next(hexa)
    
    # Search
    found = False
    while not found:
        hex_num = next(hexa)
        print(hex_num)
        while pent_num < hex_num:
            pent_num = next(pent)

        if hex_num == pent_num:
            while tri_num < pent_num:
                tri_num = next(tri)
            
            if pent_num == tri_num:
                found = True

    print(tri_num, pent_num, hex_num)


if __name__=="__main__":
    main()