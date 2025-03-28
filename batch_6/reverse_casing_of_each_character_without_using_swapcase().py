# Ask for user input
text = input("Enter a phrase: ")

# Mimic swap case functionality using loop and conditional demands
swapped_text = "".join([character.upper() if character.islower() else character.lower() for character in text])

# Print result 
print("Output:", swapped_text)