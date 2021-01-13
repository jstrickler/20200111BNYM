fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

# SORTED_LIST = sorted(ITERABLE)
# SORTED_LIST = sorted(ITERABLE, key=SOME_FUNCTION)

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(f):
    return f.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def len_and_name(f):
    return  len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print("f4:", f4, '\n')

def wacky(x):
    print("in wacky(): x is", x)
    return x[-1]

f5 = sorted(fruits, key=wacky)
print("f5:", f5, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    first_name, last_name, product, dob = person
    return dob

for person in sorted(people, key=by_dob):
    print(person)
print()

def ln_fn(p):
    return p[1], p[0]

for person in sorted(people, key=ln_fn):
    print(person)
print()

# sort by product (3rd field)
for person in sorted(people, key=lambda p: p[2]):
    print(person)
print()

# lambda params: return-value
f6 = sorted(fruits, key=lambda x: x.lower())
print("f6:", f6, '\n')

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in sorted(airports.items()):
    print(code, name)
print("=" * 60)

def by_value(e):
    return e[1]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print("=" * 60)

print(airports.items())

f7 = sorted(fruits, key=lambda f: f.lower(),  reverse=True)
print("f7:", f7, '\n')
