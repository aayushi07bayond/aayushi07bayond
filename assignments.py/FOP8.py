a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

if a == b or a + b == 5 or abs(a - b) == 5:
    result = True
else:
    result = False

print("Result:", result)
