# Project Euler
# Problem 36: Double-base Palindromes

def is_palindrome(num_str):
    if num_str == num_str[::-1]:
        return True
    return False

if __name__=="__main__":
    double_palindromes = []
    for n in range(1_000_000):
        if is_palindrome(str(n)):
            binary = bin(n)
            if is_palindrome(binary[2:]):
                double_palindromes.append(n)
    print(sum(double_palindromes))
