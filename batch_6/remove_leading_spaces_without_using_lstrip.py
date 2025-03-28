# Ask for user input
full_name = input("Enter your full name beginning with space(s): ")

# Remove the spaces
index = 0
while index < len(full_name) and full_name[index] == " ":
    index += 1

formatted_name = full_name[index:] # Starts from the non-space character

# Print result
print("Output:", formatted_name)