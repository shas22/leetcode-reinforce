# n = number to do factorial
def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)

#fun fact python has a recursion max depth, which 1000 it seems