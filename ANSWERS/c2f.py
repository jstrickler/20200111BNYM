#!/usr/bin/env python
temp_str = input("Enter Celsius temp: ")

try:
    celsius = float(temp_str)
except ValueError as err:
    print("Please only enter numbers")
else:
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{:,.2f} C is {:,.2f} F".format(celsius, fahrenheit))

