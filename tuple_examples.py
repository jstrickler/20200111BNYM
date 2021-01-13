
person = ('Bill', 'Gates', 'Microsoft', '1955-10-24')

person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

pos = 5, 8

city = 'Des Moines', 'IA'

print(person[0], person[-1], len(person))

first_name, last_name, product, dob = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

for first_name, last_name, *products, dob in people:
    # first_name, last_name, product, dob = <next element of> people
    print(first_name, last_name, products)
print()

values = [1, 2, 3, 4, 5, 6]

a, b, *c = values
print(a, b, c)

a, *b, c = values
print(a, b, c)

*a, b, c = values
print(a, b, c)