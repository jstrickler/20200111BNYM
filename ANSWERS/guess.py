#!/usr/bin/env python

max_value = 100001
min_value = 0
tries = 1

while True:
    guess = (max_value + min_value) // 2
    answer = input("Is {} your number? ".format(guess))

    if answer == "q":
        break

    if answer == "h":
        max_value = guess
    # else if
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        print("I got it in {} tries!".format(tries))
        break
    else:
        print("Please enter h, l, y, or q")

    if answer in "hl":
        tries += 1  # tries = tries + 1
