def remove_chars(word, n):
    print("Original string:", word)
    x = word[n:]
    return x

string = input("Enter a string: ")
remove = int(input("Enter number where to remove: "))

result = remove_chars(string, remove)
print("Final string:", result)
