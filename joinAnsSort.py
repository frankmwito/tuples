# combine two tuples and sort the resulting tuple in ascending order

num1 = int(input("Enter the  size of your tuple:"))
numbers1 = tuple()

num2 = int(input("Enter the  size of your tuple:"))
numbers2 = tuple()

for i in range(num1):
    number1 = input(f"Enter any number {i+1}:")
    numbers1 += (int(number1),)
    
print(numbers1)

for i in range(num2):
    number2 = input(f"Enter any number {i+1}:")
    numbers2 += (int(number2),)
    
print(numbers2)

super_tuple = numbers1 + numbers2

print(f"The joined and sorted tuple is: {sorted(super_tuple)}")