# Project Euler
# Problem 33: Digit cancelling fractions

def product_denominator(fractions):
    numerators, denominators = [], []
    for fraction in fractions:
        a, b = fraction
        numerators.append(a)
        denominators.append(b)

    num_result, den_result = 1, 1
    for num in numerators:
        num_result *= num
    for den in denominators:
        den_result *= den

    return (num_result, den_result)


def solve():
    fractions = []
    for a in range(10, 100):
        for b in range(10, 100):
            # 1 or greater
            if a >= b:
                continue

            numerator = set(str(a))
            denominator = set(str(b))

            # Filter trivial examples
            if ('0' in numerator or '0' in denominator or 
                numerator == denominator or
                len(numerator) == 1 or
                len(denominator) == 1):
                continue

            c = int(''.join(numerator - denominator))
            d = int(''.join(denominator - numerator))
            if c < 10 and d < 10 and (a/b) == (c/d):
                fractions.append((a, b))

    print(fractions)
    print(product_denominator(fractions)) # therefore 1/100, solution: 100

if __name__=="__main__":
    solve()