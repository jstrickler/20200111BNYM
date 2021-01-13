fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800,80,1000,32,255,400,5,5000]

print(len(fruits), len(nums))
print(min(fruits), max(fruits), min(nums), max(nums))
print(sorted(fruits))
print(sorted(nums))

print(sum(nums))

rfruits = reversed(fruits)
print(rfruits)
for fruit in rfruits:
    print(fruit)
print()

# print(len(rfruits), rfruits[0])  # NOT POSSIBLE

actor = 'Chris Hemsworth'
for char in reversed(actor):
    print(char.upper(), end='')
print()

for i, fruit in enumerate(fruits):
    print(i, fruit)

e = enumerate(fruits)
print(e)
for i, fruit in e:
    print(i, fruit)

for i in range(5):    #  range(STOP) range(START, STOP)
    print("PYTHON ROCKS!")
print()

for i in range(1, 11):
    print(i, "OK")

i = 1
while i < 11:
    print(i, "OK")
    i += 1

# for i in range(len(fruits)):
#     print(fruits[i])

for fruit in fruits:
    print(fruit)

for i in range(97, 123):
    print(chr(i), end='')
print()

# CA, "Fresno, Sacrmento", 23802
import csv






