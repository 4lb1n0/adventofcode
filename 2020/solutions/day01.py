# --- Day 1: Report Repair ---

# --- PART 01 ---
# In expense report find the two entries that sum to 2020; what do you get if you multiply them together?

from itertools import combinations
report = []
file = open("report.txt")
lines = file.readlines()
for line in lines:
    report.append(int(line.strip()))
print(*(i[0]*i[1] for i in combinations(report, 2) if sum(i) == 2020))

# --- PART 02 ---
# In expense report, what is the product of the three entries that sum to 2020?

from itertools import combinations
report = []
file = open("report.txt")
lines = file.readlines()
for line in lines:
    report.append(int(line.strip()))
print(*(i[0]*i[1]*i[2] for i in combinations(report, 3) if sum(i) == 2020))
