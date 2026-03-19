# This is a simple Python program that demonstrates variable assignment and type checking.

name="Anubhav"
age=20
price=100.50
print("My name is", name)
print("My age is", age)
print("The price is", price)
print(type(name))
print(type(age))
print(type(price))

# Now let's perform some arithmetic operations

a=10
b=20    
sum=a+b
print("The sum of a and b is", sum)
print(type(sum))
difference=a-b
print("The difference of a and b is", difference)
print(type(difference))
product=a*b
print("The product of a and b is", product)     
print(type(product))
quotient=a/b
print("The quotient of a and b is", quotient)   
print(type(quotient))

#  relational operators
x=50
y=20 
print("Is x greater than y?", x>y)
print("Is x less than y?", x<y)     
print("Is x equal to y?", x==y)
print("Is x not equal to y?", x!=y)   

#create a variable by the name of my_var and assign it an integer value. Then, print the data type of my_var. Next, reassign my_var with a string value and print the updated data type.

my_var=50  # Assign an integer value to my_var.
print(type(my_var))  # Print the current data type of my_var (int).
my_var="Hello"  # Reassign my_var with a string value.
print(type(my_var))  # Print the updated data type of my_var (str).


# Create two variables, num1 and num2, and assign them the same integer value. Then, print the memory addresses of both variables and check if they refer to the same object in memory.

num1=500
num2=500
print("Memory address of num1:", id(num1))  # Print the memory address of num1.
print("Memory address of num2:", id(num2))  # Print the memory address of num2.
print("Are num1 and num2 the same object?", num1 is num2)  # Check if num1 and num2 refer to the same object in memory.
print(id(num1) == id(num2))  # Check if the memory addresses of num1 and num2 are the same. 


x=input("enter your age:")  # Prompt the user to enter their age and store it in variable x.
print("Your age is", x)  # Print the age entered by the user.

#WAP to take input 2 nubers from user and print their sum, difference, product and quotient.
num1=int(input("Enter the first number: "))  # Take the first number as input from the user and convert it to an integer.
num2=int(input("Enter the second number: "))  # Take the second number as input from the user and convert it to an integer.
sum=num1+num2  # Calculate the sum of num1 and num2.
difference=num1-num2  # Calculate the difference of num1 and num2.
product=num1*num2  # Calculate the product of num1 and num2.
quotient=num1/num2  # Calculate the quotient of num1 and num2.
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)    

#WAP to take two varable and swap their values without using a third variable.
a=10
b=20    
print("Before swapping: a =", a, "b =", b)  # Print the values of a and b before swapping.
a=a+b  # Update a to be the sum of a and b.
b=a-b  # Update b to be the difference of the new a and the original b.
a=a-b  # Update a to be the difference of the new a and the new b.
print("After swapping: a =", a, "b =", b)  # Print the values of a and b after swapping.

a=10
b=20  
a,b = b, a  # Swap the values of a and b using tuple unpacking.)
print( a,  b)  # Print the values of a and b after swapping.

#WAP to take two numbers from user and print their sum.


x=int(input("enter the first number:"))
y=int(input("enter the second number:"))    
sum= x + y 
print("the sum of x and y is:",sum)    

#WAP to take a number from user and check whether it is positive or non-positive.


