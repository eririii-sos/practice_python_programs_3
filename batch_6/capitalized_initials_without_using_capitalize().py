# Ask for user input
text = input("Enter text: ")

# Convert first letter to uppercase and the rest to lowercase manually
if text:
    capitalized_text = text[0].upper() + text[1:].lower()
else:
    capitalized_text = text

# Print result
print("Output:", capitalized_text)