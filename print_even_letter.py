word = input("Enter a word : ")

print(f"Original string is :{word}")
size = len(word)

print("Printing.. only Even character : ")

for i in range(1, size-1, 2):
    print("index[", i+1, "]", word[i])