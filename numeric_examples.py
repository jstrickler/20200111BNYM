
# int float boolean complex

i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100
print(i1, i2, i3, i4)

i5 = 29302852309582039582039582039582093582093582093582093850298350298350293850928350
print(i5 + 1)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.2343e22
print(f1, f2, f3, f4)
print()

a = 23
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)  # exponent
print(a % b)  # modulus (remainder)
print()
print(divmod(a, b))

x = 10
x += 2  # x = x + 2
x /= 3  # x = x / 3
x *= 25
print(x)

# NOT supported
#  x++ ++x  etc.

# P E M D A S

a = "  123   "
b = 456

print(int(a) + b)
print(a + str(b))

# int() str() bool() float()

