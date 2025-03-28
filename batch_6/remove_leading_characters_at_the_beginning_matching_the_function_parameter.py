# Ask for user input
text = input("Enter a word: ")
prefix = input("Enter the prefix to remove: ")

# Check if the input starts with entered prefix and remove it manually
if text.startswith(prefix):
    text = text[len(prefix):]

# Print result
print("Output:", text)