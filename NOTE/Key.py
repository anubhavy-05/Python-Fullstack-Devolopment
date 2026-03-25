# QUESTION 1

from tkinter.messagebox import QUESTION
from unittest import result


x=int(7.9) # Typecasting a float to an integer, which will truncate the decimal part and give 7.truncation means that the decimal part is removed and only the whole number part is kept.
print(x) # Output: 7

# QUESTION 2

y=float(7) # Typecasting an integer to a float, which will give 7.0.
print(y) # Output: 7.0

# round() is a built-in function in Python that rounds a number to a specified number of decimal places. If the number of decimal places is not specified, it rounds to the nearest integer.rules of rounding: If the decimal part is less than 0.5, the number is rounded down. If the decimal part is 0.5 or greater, the number is rounded up.

# QUESTION 3

z=round(7.8) # Rounds to the nearest integer.
print(z) # Output: 8
z=round(7.8, 1) # Rounds to 1 decimal place.
print(z) # Output: 7.8


# QUESTION 4

age = 20
text = "Age: "
result = text + str(age) # Typecasting the integer age to a string and concatenating it with the text.

print(result) # Output: "Age: 20"

print(f"{text}{age}")

pi = 3.14159
print(f"Value: {pi:.2f}") # Output: 3.14 (sirf 2 decimal tak)

salary = 50000
print(f"Salary: {salary:,}") # Output: 50,000 (comma lag jayega)

# QUESTION 5

#WAP using f-string to Hii ! Mera name Anubhav hai aur mera lucky number 7 hai. Take the name and lucky number as input from the user.

name="Anubhav"
lucky_number=7
print(f"Hi! My name is {name} and my lucky number is {lucky_number}.")

                        #  OR

#WAP using f-string to Hii ! Mera name Anubhav hai aur mera lucky number 7 hai. Take the name and lucky number as input from the user.

name = input("Enter your name: ")
lucky_number = int(input("Enter your lucky number: "))
print(f"Hi! My name is {name} and my lucky number is {lucky_number}.")


# QUESTION 6

score = 0
result=score or "No score" # If score is 0, it will return "No score". If score is any non-zero value, it will return the score itself.
print(result) # Output: "No score" because 0 is considered False in Python.











 
