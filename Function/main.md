


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



                  # difference between function and method:

# A function is a block of code that performs a specific task and can be called independently. It can be defined using the def keyword and can be used in various contexts. For example, the built-in print() function is a function that can be called to display output.

# A method is a function that is defined inside a class and is called on an instance of that class. It has access to the data and methods of the class instance. For example, if we have a class called MyClass with a method called my_method(), we can create an instance of MyClass and call my_method() on that instance. The method can access the attributes and other methods of the class instance. 



                # difference between defining a function and calling a function:

# defining a function means creating the function and specifying its name, parameters, and the code block that it will execute when called. calling a function means executing the code inside the function by using its name followed by parentheses, and optionally passing arguments to it. defining a function does not execute the code inside it, while calling a function does execute the code inside it.for example: 

def greet(name):              # this is defining a function named greet that takes a parameter name.
    return "Hello, " + name + "!" # this is the code block that will be executed when the function is called. it returns a greeting message using the name parameter.   
print(greet("Alice"))     # this is calling the function greet with the argument "Alice". it executes the code inside the function and returns the greeting message which is then printed..output: "Hello, Alice!" (the function is called with the argument "Alice", and it returns the greeting message which is then printed)
