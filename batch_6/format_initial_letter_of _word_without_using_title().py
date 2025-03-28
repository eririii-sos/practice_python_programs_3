# Ask for user input
text = input("Enter a phrase: ")

# Format first letter of each word to uppercase and the rest to lowercase
words = text.split() # Split the string into words
capitalized_words = [word[0].upper() + word[1:].lower() if word else '' for word in words]

# Join the words back 
output = " ".join(capitalized_words)

# Print result
print("Output:", output)