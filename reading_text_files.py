import os
import paramiko

file_name = 'DATA/mary.txt'
print(os.path.abspath(file_name))

mary_in = open(file_name)
# read file ...
mary_in.close()

with open(file_name) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # removes trailing \n
        print(line)
    # mary_in.close()
print('-' * 60)

with open(file_name) as mary_in:
    contents = mary_in.read() # read whole file
    print("NORMAL:")
    print(contents)
    print()
    print("RAW:")
    print(repr(contents))
print('-' * 60)

with open(file_name) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open(file_name) as mary_in:
    all_lines = mary_in.read().splitlines()
    print(all_lines)

for line in all_lines:
    print(line.upper()[:8])
