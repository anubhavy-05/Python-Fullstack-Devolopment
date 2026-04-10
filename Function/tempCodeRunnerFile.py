def fibonacci(n):
    if n <= 0:
        return 0 # the Fibonacci of 0 is defined to be 0
    elif n == 1:
        return 1 # the Fibonacci of 1 is defined to be 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # this is a recursive call to calculate the Fibonacci of n by summing the Fibonacci of (n-1) and (n-2)       
print(fibonacci(10)) 