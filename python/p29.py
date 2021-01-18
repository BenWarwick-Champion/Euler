# Project Euler
# Problem 29: Distinct Powers

if __name__ == "__main__":
    distinct = set([a**b for a in range(2, 101) for b in range(2, 101)])
    print(f"There are {len(distinct)} distinct terms.")
