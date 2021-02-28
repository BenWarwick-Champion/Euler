# Project Euler
# Problem 48: Self Powers

def self_powers():
    result = sum([n**n for n in range(1, 1001)])
    print(str(result)[-10:])

if __name__=="__main__":
    self_powers()