string = input("Enter a string: ")

character_frequency = {}

# Count the frequency of each character in the string
for char in string:
    if char in character_frequency:
        character_frequency[char] += 1
    else:
        character_frequency[char] = 1

# Print the character frequency
print("Character frequency in the string:")
for char, frequency in character_frequency.items():
    print(char, ":", frequency)
