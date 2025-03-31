# ASk for user input
text = input("Enter text: ")
substring = input("Enter the substring  to count: ")

# Count occurences of the substring manually
count = 0
for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        count += 1

# Print result
print(f"The substring appears {count} times in the text.")