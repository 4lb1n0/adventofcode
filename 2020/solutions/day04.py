# --- Day 4: Passport Processing ---
''' Passport data is validated in batch files (your puzzle input).
Each passport is represented as a sequence of key:value pairs separated by spaces or newlines.
Passports are separated by blank lines.'''

# --- PART 01 ---
# Count the number of valid passports - those that have all required fields. Treat cid as optional.
# In your batch file, how many passports are valid?

file = open("day04.txt")
passports = file.read().split("\n\n")
passports = [i.replace("\n", " ").split(" ") for i in passports]
passports = [dict(i.split(":") for i in j) for j in passports]

counter = 0
for passport in passports:
    if len(passport.keys()) > 7:
        counter += 1
    elif len(passport.keys()) == 7 and "cid" not in passport.keys():
        counter += 1

print(counter) # 250 in our case

# --- PART 02 ---

''' Your job is to count the passports where all required fields are both present and valid according to the rules'''

# Count the number of valid passports - those that have all required fields and valid values.
# Continue to treat cid as optional. In your batch file, how many passports are valid?

file = open("input.txt")
passports = file.read().split("\n\n")
passports = [i.replace("\n", " ").split(" ") for i in passports]
passports = [dict(i.split(':') for i in j) for j in passports]

required_fields = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: len(x) == 7 and x[0] == "#" and str(x[1:7]).isalnum(),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9
}

counter = 0
for passport in passports:
    for key, value in required_fields.items():
        if len(passport.keys()) < 7: break
        elif len(passport.keys()) == 7 and "cid" in passport: break
        if not value(passport[key]):
            break
    else: counter+=1

print(counter) # 158

