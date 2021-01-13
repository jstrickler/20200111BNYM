import os

with os.popen('hostname') as hostname_in:
    raw_hostname = hostname_in.read()

hostname = raw_hostname.rstrip()
print("hostname is", hostname)

