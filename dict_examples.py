d1 = dict() # empty dict
d2 = {'red': 1, 'green': 55, 'purple': 15}

state_caps = {'PA': "Harrisburg", 'NJ': 'Trenton', 'NY': 'Albany', 'DE': 'Dover'}
print(d2['red'])
print(state_caps['NJ'])

print(state_caps.get('NC'))
print(state_caps.get('NC', 0))

print(state_caps.get('NC', "rutabaga"))

state_caps['MD'] = 'Annapolis'

print(state_caps)

print(state_caps.get('MD'))
print(state_caps.get('CA', 'ooooooh'))

for abbr, state in state_caps.items():
    print(abbr, state)

print(state_caps.items())

print(state_caps.keys())
print(state_caps.values())

more_caps = {'VA': 'Richmond', 'NC': 'Raleigh', 'MD': 'Baltimore'}

# traditional
state_caps.update(more_caps)
# state_caps |= more_caps
print(state_caps)

for k in 'VA', 'PA', 'TX', 'ID', 'MD':
    if k in state_caps:
        print(state_caps[k])

del state_caps['MD']
print(state_caps)

for k, v in state_caps.items():
    print(k, v.upper())
