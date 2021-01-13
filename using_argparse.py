# python using_argparse.py -f myfile
import argparse  # find and load argparse.py

parser = argparse.ArgumentParser(description="Class Example of Option Parsing")

parser.add_argument("-f", dest="filename",  help="File to open")

args = parser.parse_args()

print(args)
print(args.filename)