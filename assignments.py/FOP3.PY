n = int(input("Enter the range: "))

fibonacci_series = [0, 1]  # Initialize the Fibonacci series with the first two numbers

# Generate the Fibonacci series using a for loop
for i in range(2, n):
    next_num = fibonacci_series[i-1] + fibonacci_series[i-2]
    fibonacci_series.append(next_num)

# Print the Fibonacci series
print("Fibonacci series within the given range:")
for num in fibonacci_series:
    print(num, end=" ")
