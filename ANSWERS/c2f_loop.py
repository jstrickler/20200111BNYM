#!/usr/bin/env python

while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32
    print('{:.1f}\u00B0 C is {:.1f}\u00B0 F\n'.format(celsius, fahrenheit))

