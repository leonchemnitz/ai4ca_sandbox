// a function that calculates the sum of two numbers
def sum(a, b):
    return a + b

// a function that calculates the difference of two numbers
def diff(a, b):
    return a - b

// a function that calculates the product of two numbers
def product(a, b):
    return a * b

// a function that calculates the quotient of two numbers
def quotient(a, b):
    return a / b

//calculate the fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
