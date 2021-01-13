fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + "\n")

with open('DATA/primeministers.txt') as pm_in:
    with open('pm_parties.txt', 'w') as pm_out:
        for raw_line in pm_in:
            line = raw_line.rstrip()
            term, first_name, last_name, dob, dod, place_of_birth, took_office, left_office, party = line.split(':')
            wombat = f"{last_name}\t{party}\n"
            wombat = "{}\t{}\n".format(last_name, party)
            pm_out.write(wombat)
