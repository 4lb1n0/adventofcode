# --- Day 2: Password Philosophy ---
''' PASSWORD POLICY START
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
    PASSWORD POLICY END'''

# --- PART 01 ---
# How many passwords are valid according to their policies?

file = open("day02.txt")
lines = file.readlines()
valid_passwords = 0
for line in lines:
    wanted_letter_by_policy = line.split()[2].count(line.split()[1].strip(":")) # Here we get number of occurences of a letter by policy in given password
    first_limit = int(line.split()[0].split("-")[0]) # Here we get the minimum number of occurences
    last_limit = int(line.split()[0].split("-")[1]) # Here we get the maximum number of occurences
    if first_limit <= wanted_letter_by_policy and wanted_letter_by_policy <= last_limit:
        valid_passwords += 1

print(valid_passwords)

# --- PART 02 ---

''' NEW PASSWORD POLICY START
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.'''

# How many passwords are valid according to the new interpretation of the policies?

file = open("day02.txt")
lines = file.readlines()
valid_passwords = 0
for line in lines:
    wanted_letter_by_policy = line.split()[1].strip(":")  # Here we get needed letter by policy
    first_position = int(line.split()[0].split("-")[0]) - 1  # Here we get the first position -1 for index as TCP have no concept of "index zero"
    second_position = int(line.split()[0].split("-")[1]) - 1  # Here we get the second position -1 for index as TCP have no concept of "index zero"
    password = line.split()[2]  # We get letters in password

    # In lines bellow we check if first position or second position is wanted letter and if it is we add 1 as a valid password
    valid_passwords += 1 if (password[first_position] == wanted_letter_by_policy and
                             password[second_position] != wanted_letter_by_policy) else 0

    valid_passwords += 1 if (password[first_position] != wanted_letter_by_policy and
                             password[second_position] == wanted_letter_by_policy) else 0

print(valid_passwords)
