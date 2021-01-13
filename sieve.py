
limit = 101

flags = [True] * limit

print(flags)

for num_to_check in range(2, limit):
    if flags[num_to_check]:  # number is prime
        print(num_to_check, end=' ')  # display it
        for i in range(num_to_check * 2, limit, num_to_check):
            flags[i] = False
print(flags)