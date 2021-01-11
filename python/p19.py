# Project Euler
# Problem 19: Counting Sundays

import datetime

if __name__ == "__main__":
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            date = datetime.date(year, month, 1)
            if date.weekday() == 6:
                count += 1
    print(f"There are {count} Sundays that fall on the 1st of the month.")