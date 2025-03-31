# Ask user for input
text = input("Enter text: ")

# Check if all characters are lowercase manually
lower_case = all('a' <= character <= 'z' or not character.isalpha() for character in text)

# Print result
print("Are all the characters in lowercase?", lower_case)