# Project Euler
# Problem 32: Pandigital Primes

def solve():
    products = set()
    digit_set = set('123456789')
    
    for x in range(1, 100):
        for y in range(100, 10_000):
            digits = str(x) + str(y) + str(x*y)
            if len(digits) == 9 and set(digits) == digit_set:
                products.add(x*y)
    
    print(f"Sum of pandigital products is: {sum(products)}")    # 45228

if __name__=="__main__":
    solve()
