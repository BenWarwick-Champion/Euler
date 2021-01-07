# Project Euler
# Problem 14: Longest Collatz sequence

def next_collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def find_steps(n):
    steps = 0
    while n != 1:
        if n in memory:
            steps += memory[n]
            return steps
        n = next_collatz(n)
        steps += 1
    steps += 1
    return steps

if __name__ == "__main__":
    memory = {}
    max_steps, max_start = 0, 0
    
    for i in range(500_000, 1_000_000):
        memory[i] = find_steps(i)
        if memory[i] > max_steps:
            max_steps = memory[i]
            max_start = i

    print(f"Starting number to produce the longest sequence: {max_start}")
        