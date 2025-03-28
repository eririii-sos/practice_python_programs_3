# Ask for user input
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Add spaces at the end to match the total width
formatted_text = text + " " * (width - len(text)) if len(text) < width else text

# Print result
print(f"Output:|{formatted_text}|")