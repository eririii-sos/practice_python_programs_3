# Ask for user input
word = input("Enter a word: ")
suffix = input("Enter the suffix to remove: ")

# Check if the input ends with entered suffix and remove it manually
if word.endswith(suffix):
    word = word[:len(word) - len(suffix)]

# Print result
print("Output:", word)