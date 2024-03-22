#!/usr/bin/python3

def minOperations(n):
    if n < 2:
        return 0
    
    operations = 0
    copied = 1
    buffer = 1

    while copied < n:
        if n % copied == 0:
            buffer = copied
            operations += 1
        copied += buffer
        operations += 1

    return operations

# Example usage:
n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))  # Output: 4

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))  # Output: 7
