
#WAP to calculate the area of a rectangle. Take the length and breadth as input from the user.

Length=int(input("Enter "))
breath=int(input("Enter "))
area=Length*breath
print("The area of the rectangle is:", area)



#WAP TO REMOVE THE LAST DIGIT FROM A NUMBER. TAKE THE NUMBER AS INPUT FROM THE USER.

number=int(input("Enter a number:"))
result=number//10
print("The number after removing the last digit is:", result)

#WAP to swap two numbers without using a third variable. Take the two numbers as input from the user.

a=int(input("Enter the first number:")) 
b=int(input("Enter the second number:"))
a,b=b,a
print("The value of a is:", a)
print("The value of b is:", b)

                 #OR
a=a+b
b=a-b
a=a-b
print("The value of a is:", a)
print("The value of b is:", b)

                  #OR
a=5
b=10
a,b=b,a
print("The value of a is:", a)
print("The value of b is:", b)

#WAP to check if a number is divisible by 5. Take the number as input from the user.

x=int(input("Enter a number:"))
if x%5==0:
    print("The number is divisible by 5.")



#WAP to check wheather a nuber is three digit or not. Take the number as input from the user.

number=int(input("Enter a number:"))
if 100<=number<=999:
    print("The number is a three-digit number.")

#WAP to check how many digits are there in a number. Take the number as input from the user.
number=int(input("Enter a number:"))
digit_count=len(str(number))
print("The number of digits in the number is:", digit_count)


