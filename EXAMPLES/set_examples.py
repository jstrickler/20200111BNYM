#!/usr/bin/env python

set1 = {'red', 'blue', 'green', 'purple', 'green'}  # <1>
set2 = {'green', 'blue', 'yellow', 'orange'}
more_colors = ['pink', 'green', 'orange', 'red']
set3 = set(more_colors)

set1.add('taupe')  # <2>

print("set 1:", set1)
print("set 2:", set2)
print("&", set1 & set2)  # <3>
print("|", set1 | set2)  # <4>
print("^", set1 ^ set2)  # <5>
print("s1 - s2", set1 - set2)  # <6>
print("s2 - s1", set2 - set1)
print()

food = 'spam ham ham spam spam spam ham spam spam eggs cheese spam'.split()
print(food)
food_set = set(food)  # <7>
print(food_set)

parties = set()
with open('../DATA/primeministers.txt') as pm_in:
    for raw_line in pm_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        party = fields[-1]
        parties.add(party)

print(parties)