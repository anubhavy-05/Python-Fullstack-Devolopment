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
print(memory  address of num1:", id(num1))  # Print the memory address of num1.
print("Memory address of num2:", id(num2))  # Print the memory address of num2.
print("Are num1 and num2 the same object?", num1 is num2)  # Check if num1 and num2 refer to the same object in memory.
print(id(num1) == id(num2))  # Check if the memory addresses of num1 and num2 are the same. 
