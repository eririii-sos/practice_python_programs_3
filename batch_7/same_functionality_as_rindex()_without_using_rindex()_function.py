# Ask for user input
text = input("Enter text: ")
substring = input("Enter the substring to find: ")

# Find the last occurrence of the substring manually
index = -1
for i in range(len(text) - len(substring), -1, -1):
    if text[i:i+len(substring)] == substring:
        index = 1
        break

# Print result
if index != -1:
    print(f"The substring last appears at index {index}.")
else:
    print("Error! Substring not found.") # Error handling