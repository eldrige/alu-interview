#!/usr/bin/python3
def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    current = 1

    for i in range(2, n + 1):
        while n % i == 0:  # i is a factor of n
            operations += i  # Copy All (1 operation) + Paste (i-1 operations)
            n //= i  # Reduce n by the factor i

    return operations


# Example usage:
print(minOperations(9))  # Output: 6
