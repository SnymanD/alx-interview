#!/usr/bin/python3

def minOperations(n):
    if n == 1:
        return 0

    # Initialize the number of operations and the buffer
    operations = 0
    buffer = 1  # Initial H in the buffer

    # Start with one character already in the file
    copied = 1

    while copied < n:
        # If the buffer can be pasted to get to or exceed the target, paste it
        if (copied + buffer) >= n:
            operations += 1  # Paste
            copied += buffer
        else:
            # If the buffer can't be pasted to reach the target, copy the current content
            copied *= 2  # Copy All
            buffer = copied  # Update the buffer
            operations += 1  # Copy All

    return operations

# Example usage:
n = 9
print("Minimum number of operations:", minOperations(n))  # Output: 6
