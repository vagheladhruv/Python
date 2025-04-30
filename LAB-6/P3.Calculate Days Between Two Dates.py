'''
Suppose a date is represented as a tuple (d, m, y).
 Create two date tuples and find the number of days between the two dates.
'''

from datetime import date

date1 = (12, 5, 2023)  # d, m, y
date2 = (15, 6, 2023)
d1 = date(*reversed(date1))
d2 = date(*reversed(date2))
delta = d2 - d1
print(f"Number of days between {date1} and {date2}: {delta.days}")