sentence = input("Enter a sentence: ")
words = sentence.split()

word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequency in the sentence:")
for word, frequency in word_frequency.items():
    print(word, ":", frequency)
