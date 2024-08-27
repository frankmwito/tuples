# create a tuple from a list of integers and find the maximum and minimum values in the tuple

num = int(input("Enter any number for the size of the list:"))
numbers = list()

for i in range(num):
    numbers.append(int(input(f"Enter any number {i+1}:")))

print("your list is", numbers)

numbers1 = tuple(numbers)

max_value = max(numbers1)
print(max_value)
min_value = min(numbers1)
print(min_value)
