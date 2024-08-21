def fibonacci_sequence(n):
    # Initialize variables for the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Get user input for the number of terms
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Display the Fibonacci sequence up to the specified number of terms
print("Fibonacci sequence:")
print(fibonacci_sequence(num_terms))