
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

print("It's the best language")
print('Python is the "best" language')
print("'Hello NY' is what I said")
# print("this is \"tricky\" and hard to read")
# print("Python is the \"best\" language")

print("""Guido's the "BDFL" of Python""")
print(r"This is a backslash: \ ")
print()

actor = "Chris Hemsworth"
print(type(actor), len(actor))

print(actor.upper())
a = actor.upper()
print(a, actor)
print(actor.lower())

print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'), actor.startswith('Liam'))
print("wor" in actor)
print("row" in actor)
print(actor.replace('Chris', 'Liam'))

s = "       Wherever you go, there you are.     "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s2 = "The snake says Hiss............"
print(s2.rstrip('.'))
s3 = "Blah blah blah!;,."
print(s3.rstrip('.;,!'))

s4 = "xyxxxxxxxxxyBlah fix my hexagram blah blahyyyyyyyyyyyyyyyyxyyyyyyyx"
print(s4.strip('xy'))

s = "Pack my     jug with five         dozen liquor       bottles"

words = s.split()
print(words)

s = "one\ttwo\tthree"
print(s.split('\t'))
















