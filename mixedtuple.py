# create a tuple with mixed data types (integers, strings, and floats)
# extract and print only the numeric values.

mixed_tuple = ("frank", "johnny", 22, 34, 22.34, 34.22)
found_numeric = False

for item in mixed_tuple:
    if isinstance(item, (int, float)):
        print(item)
        found_numeric = True
if not found_numeric:
    print("No numeric values found in the tuple")