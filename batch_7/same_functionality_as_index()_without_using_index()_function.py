# Ask for user input
text = input("Enter text: ")
substring = input("Enter the substring to find: ")

# Find the first occurrence of the substring manually
index = -1
for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        index = i
        break

# Print result
print(f"The substring first appears at index {index}.") 