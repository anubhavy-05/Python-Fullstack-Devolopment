

                          # FUNCTION IN PYTHON


#function: it is a block of code which only runs when it is called. you can pass data, known as parameters, into a function. a function can return data as a result.    
# and it is reusable. also it helps to break our program into smaller and modular chunks. it makes the code more organized and manageable.
# syntax of function:
# def function_name(parameters):
#     # code block
#     return value  
# example of function:  
def greet(name):
    return "Hello, " + name + "!" # this function takes a name as a parameter and returns a greeting message.   
print(greet("Alice")) # Output: "Hello, Alice!" (the function is called with the argument "Alice", and it returns the greeting message which is then printed)



# EXAMPLE 2:
def add(a, b):
    return a + b # this function takes two parameters a and b, and returns their sum.
print(add(5, 3)) # Output: 8 (the function is called with the arguments 5 and 3, and it returns their sum which is then printed)

# EXAMPLE 3:

def is_even(num):
    return num % 2 == 0 # this function takes a number as a parameter and returns True if the number is even, otherwise it returns False.   
print(is_even(4)) # Output: True (the function is called with the argument 4, and it returns True since 4 is even)
print(is_even(5)) # Output: False (the function is called with the argument 5, and it returns False since 5 is not even)        

# EXAMPLE 4:

def factorial(n):   
    if n == 0:
        return 1 # the factorial of 0 is defined to be 1
    else:
        return n * factorial(n - 1) # this is a recursive call to calculate the factorial of n by multiplying n with the factorial of (n-1) 
print(factorial(5)) # Output: 120 (the function is called with the argument 5, and it calculates the factorial of 5 which is 5 * 4 * 3 * 2 * 1 = 120)

# EXAMPLE 5:    
def fibonacci(n):
    if n <= 0:
        return 0 # the Fibonacci of 0 is defined to be 0
    elif n == 1:
        return 1 # the Fibonacci of 1 is defined to be 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # this is a recursive call to calculate the Fibonacci of n by summing the Fibonacci of (n-1) and (n-2)       
print(fibonacci(10)) # Output: 55 (the function is called with the argument 10, and it calculates the Fibonacci of 10 which is the sum of the Fibonacci of 9 and 8) 