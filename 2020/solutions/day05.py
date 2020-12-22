# --- Day 5: Binary Boarding ---
''' You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input);
perhaps you can find your seat through process of elimination.
Instead of zones or groups, this airline uses binary space partitioning to seat people.
A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".'''

# --- PART 01 ---
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

file = open("day05.txt")
lines = file.read().split("\n")

ids = []
rows = [i for i in range(0, 128)]
columns = [i for i in range(0, 8)]

seat_id_row = []
column_id_row = []

unique_seat = []
for line in lines:
    row_id = rows[:(len(rows)//2)] if line[0] == "F" else rows[len(rows)//2:]
    column_id = columns[:(len(columns)//2)] if line[-3] == "L" else columns[len(columns)//2:]
    for let in line[1:-3]:
        row_id = row_id[:len(row_id) // 2] if let == "F" else row_id[len(row_id)//2:]
    seat_id_row.append(row_id)
    for let in line[-2:]:
        column_id = column_id[:len(column_id) // 2] if let == "L" else column_id[len(column_id)//2:]
    column_id_row.append(column_id)
    uniq = row_id[0]*8+column_id[0]
    unique_seat.append(uniq)

print(max(unique_seat)) # 888

# --- PART 02 ---
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
# What is the ID of your seat?

my_seat = sorted(unique_seat)
for i in range(0, len(my_seat)-1):
    if my_seat[i] == my_seat[i+1]-2:
        print(my_seat[i]+1)
