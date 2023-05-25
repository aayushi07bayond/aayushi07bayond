string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swap the first two characters of each string
new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

# Combine the modified strings with a space separator
result = new_string1 + " " + new_string2

print("Combined string with swapped characters:", result)
