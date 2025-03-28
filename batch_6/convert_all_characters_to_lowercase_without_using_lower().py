# Ask for user input
text = input("Enter a phrase: ")

# Format all uppercase characters to lowercase
lower_case = "".join(chr(ord(character) + 32) if 'A' <= character <= 'Z' else character for character in text)

# Print result
print("Output:", lower_case)