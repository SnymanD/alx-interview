# Pascal Triangle
# Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n.
# Returns an empty list if n <= 0
# You can assume n will be always an integer

# Pascal’s triangle
def printPascal(n):
    for line in range(0, n):
        for i in range(0, line + 1):
            print(binomialCoeff(line, i), " ", end="")
        print()
        
def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res

# Driver program
n = int(input("Enter the number of rows: "))
printPascal(n)