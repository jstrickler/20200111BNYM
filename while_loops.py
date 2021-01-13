
while True:
    user_name = input("What is your username (or q to quit)? ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        print("Name can not be blank")
        continue # start loop over
    password = input("What is your password? ")
    if password == '':
        print("Password can not be blank")
        continue
    # validate password
    print("Validating...")

