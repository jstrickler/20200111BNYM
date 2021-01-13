import os

with open('DATA/mary.txt') as mary_in:
    old_text = mary_in.read()
    new_text = old_text.replace('lamb', 'gorilla')
    with open('gorilla.txt', 'w') as gorilla_out:
        gorilla_out.write(new_text)
