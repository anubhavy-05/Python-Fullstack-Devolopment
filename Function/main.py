

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

# EXAMPLE 6:

def f1():
    print("enter a number") # this function simply prints a message when called.
    n=int(input()) # it takes an input from the user and converts it to an integer.
    for e in range(1,n+1):
        print(e**2,end=" ") # it prints all the numbers from 0 to n-1 (inclusive) using a for loop.
        print() # it prints a new line after the loop is finished.
f1() # the function is called to execute the code inside it.
f1()# the function is called again to execute the code inside it once more.




# difference between defining a function and calling a function:
# defining a function means creating the function and specifying its name, parameters, and the code block that it will execute when called. calling a function means executing the code inside the function by using its name followed by parentheses, and optionally passing arguments to it. defining a function does not execute the code inside it, while calling a function does execute the code inside it.for example: 
def greet(name): # this is defining a function named greet that takes a parameter name.
    return "Hello, " + name + "!" # this is the code block that will be executed when the function is called. it returns a greeting message using the name parameter.   
print(greet("Alice")) # this is calling the function greet with the argument "Alice". it executes the code inside the function and returns the greeting message which is then printed.

