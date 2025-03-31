# Ask for user input
text = input("Enter text: ")
prefix = input("Enter the prefix to check: ")

# Check if the string starts with the given prefix manually
check_prefix = text[:len(prefix)] == prefix if len(prefix) <= len(text) else False

# Print result
print("Does the text start with the entered prefix?", check_prefix)