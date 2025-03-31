# Ask for user input
text = input("Enter text: ")

# Convert all lowercase characters to uppercase
upper_case = "".join(chr(ord(character) - 32 ) if 'a' <= character <= 'z' else character for character in text)

# Print result
print("Output:", upper_case)