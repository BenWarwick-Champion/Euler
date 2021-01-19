# Project Euler
# Problem 31: Coin Sums

# What if you need 5? (1, 2, 5 coins)
# 1, 1, 1, 1, 1
# 2, 1, 1, 1, 0
# 2, 2, 1, 0, 0
# 5, 0, 0, 0, 0

def find_ways(n, coins):
    ways = [1] + [0] * n
    for coin in coins:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    return ways[-1]

if __name__ == "__main__":
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print(find_ways(target, coins))
    
