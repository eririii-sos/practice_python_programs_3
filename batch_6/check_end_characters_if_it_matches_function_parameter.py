# Ask for user input
text = input("Enter text: ")
suffix = input("Enter the suffix to check: ")

# Check if the string ends with the given suffix manually
check_suffix = text[-len(suffix):] == suffix if len(suffix) <= len(text) else False

# Print result
print("Does the text end with the entered suffix?", check_suffix)