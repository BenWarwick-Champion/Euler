# Project Euler
# Problem 15: Lattice Paths

def gen(n,r=[]):
    for _ in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

if __name__ == "__main__":
    tri = gen(41)
    count = 0
    for line in list(tri):
        if len(line) % 2 != 0:
            count += 1
        if count == 21:
            ind = len(line) // 2
            print(line)
            print(line[ind])
            break
