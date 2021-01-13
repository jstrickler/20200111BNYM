import csv
with open('DATA/primeministers.txt') as pm_in:
    for raw_line in pm_in:
        line = raw_line.rstrip()
        term, first_name, last_name, dob, dod, place_of_birth, took_office, left_office, party = line.split(':')
        # fields = line.split(':')
        # print(fields[1], fields[2], fields[-1])
        print(first_name, last_name, party)
print()

with open('DATA/primeministers.txt') as pm_in:
    rdr = csv.reader(pm_in, delimiter=":")
    for term, first_name, last_name, dob, dod, place_of_birth, took_office, left_office, party in rdr:
        print(first_name, last_name, left_office)

