word_list = input("Enter a list of words (separated by spaces): ").split()

longest_word_length = len(max(word_list, key=len))

print("Length of the longest word:", longest_word_length)
