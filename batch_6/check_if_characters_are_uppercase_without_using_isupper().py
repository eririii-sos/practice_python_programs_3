# Ask for user input
text = input("Enter a phrase: ")

# Check if all characters are uppercase manually
upper_case = all(character >= 'A' and character <= 'Z' or not character.isalpha() for character in text)

# Print result
print("Are all the characters in uppercase?": upper_case)