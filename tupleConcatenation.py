# given a tuple of strings concatenate all the strings and print the result

num = int(input("Enter the size of your tuple:"))
words = tuple()

for i in range(num):
    word = input("Enter a word:")
    words += (word,)
    
    print("".join(words))