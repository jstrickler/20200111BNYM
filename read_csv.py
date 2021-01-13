import csv

with open('junk.csv') as junk_in:
    rdr = csv.reader(junk_in)
    for row in rdr:
        print(row)