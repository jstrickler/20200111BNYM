a = "avocado"
b = 234.325
c = 1_234_567


print(a, b, c)  #  str(a) + " " + str(b) + " " + str(c) + "\n"
#               str(a) + sep + str(b) + sep + str(c) + end
# sep   ^  ^
# end        ^
print("next")

print(a, b, c, sep=" <=> ")
print("next next")

print(a, end="BLAH")
print(b, end="WOMBAT")
print(c)

print("first", end='')
# some logic here for other output
print("last")

result = 23.7 / 6.91
print("result is", result)
print("result is", round(result, 3))
print("result is {:.3f}".format(result))
b = 91.3293042934234

print("r is {:.3f} b is {:.3f}".format(result, b))

print(f"r is {result:.3f} b is {b:.3f}")

language = "Python"
rating = "best"
print(f"{language} is the {rating} language")

print("{} is the {} language".format(language, rating))





