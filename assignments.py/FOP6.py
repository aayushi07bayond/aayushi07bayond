letter = input("Enter a letter: ")

# Convert the letter to lowercase for case-insensitive comparison
letter = letter.lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print(letter, "is a vowel.")
else:
    print(letter, "is not a vowel.")
