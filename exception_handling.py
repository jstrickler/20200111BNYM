file_name = "wombats.txt"
try:
    with open(file_name) as wombats_in:
        pass
except FileNotFoundError as err:
    print(err)


values = ['a', 'b', 'c', 'd']
try:
    print(values[8])
except IndexError as err:
    print(err)

nums = [5.3, 8.1, '8.93', 1.27, None, 0, 16.9, 'wombat', 4.4]
for n in nums:
    try:
        result = 27.6 / float(n)
    except ZeroDivisionError as err:
        print(err)
    except (ValueError, TypeError) as err:
        print(err)
    else:
        print(result)
    finally:
        pass

print("All done.")
