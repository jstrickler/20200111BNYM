
def get_message():
    return "Hello Python world"

x = get_message  # don't do this
m = get_message()  # call the function
print(m)

def spam():
    print("Hello!")

s = spam()
print(s)
print(spam())

def make_sep(char, size):
    return char * size

x = make_sep('*', 10)
print(x)

print(make_sep('-', 60))

def say_hello():
    m = get_message()
    print(m)

say_hello()

def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)
foo('a', 'b', 'c')
foo('alpha', 5.9, [1, 2, 3])
print()

def bar(a, b=10):
    print(a, b)

bar(1, 2)
bar('none')
