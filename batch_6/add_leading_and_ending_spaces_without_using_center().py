# Ask for user input
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Calculate spaces for both sides
total_spaces = max(0, width - len(text))
leading_spaces = total_spaces // 2
ending_spaces = total_spaces - leading_spaces

# Add spaces on both side
centered_text = " " * leading_spaces + text + " " * ending_spaces

# Print result
print(f"Output:|{centered_text}|")