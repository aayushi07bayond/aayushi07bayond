string = input("Enter a string: ")

if len(string) >= 3:
    if string[-3:] == 'ing':
        string += 'ly'
    else:
        string += 'ing'

print("Modified string:", string)
