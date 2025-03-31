# Ask for user input
text = input("Enter text with trailing spaces: ")

# Remove the ending spaces
index = len(text) - 1
while index >=0 and text[index] == " ":
    index -= 1

formatted_text = text[:index + 1] # Keep all characters except the ending non-space characters

# Print result
print("Output:", formatted_text)