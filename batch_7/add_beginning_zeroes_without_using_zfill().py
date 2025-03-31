# Ask for user input
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Add zeroes at the beginning to match the total width
formatted_text = "0" * (width - len(text)) + text if len(text) < width else text

# Print result
print("Output:", formatted_text)