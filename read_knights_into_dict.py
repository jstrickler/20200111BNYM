from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)

print(knight_info['Robin'])
print(knight_info['Robin'][1])
print(knight_info['Robin'][1][0])

robin = knight_info['Robin']
print(robin[0], 'Robin')
print()

for name, info in knight_info.items():
    print(info[0], name, info[1])



