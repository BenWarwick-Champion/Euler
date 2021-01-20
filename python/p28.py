# Project Euler
# Problem 28: Number of spiral diagonals

def find_diagonals(n):
    '''Finds diagonals of an n*n spiral'''
    current, line, count = n**2, n-1, 0
    diagonals = []

    while current != 1:
        diagonals.append(current)
        current -= line
        count += 1
        if count == 4:
            count = 0
            line -= 2
    diagonals.append(current)
    
    return diagonals

if __name__ == "__main__":
    n = 1001
    print(sum(find_diagonals(n)))
