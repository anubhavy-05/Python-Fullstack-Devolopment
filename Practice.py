
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


#WAP to check how many digits are there in a number. Take the number as input from the user without using the len() function.


number=int(input("Enter a number:")) # Start the counter at 0; we will increase it once per digit.
digit_count=0   # Keep removing the last digit until no digits are left.
while number>0: # Integer division by 10 removes the last digit.
    number=number//10 # Count one digit removed in this iteration.
    digit_count+=1 # Print the total number of digits found.
print("The number of digits in the number is:", digit_count)

3#WAP to check if a number is positive, negative or zero. Take the number as input from the user.

x=int(input("Enter a number:"))
if x>0:
    print("The number is positive.")
elif x<0:
    print("The number is negative.")
else:
    print("The number is zero.")

#WAP to print all the odd numbers from 1 to 20 using for loop.or wap to print first 10 odd numbers using for loop.


for i in range(1, 21):
    if i%2!=0:
        print(i)

#wap to print all the odd numbers from 1 to 20 using while loop.

i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1
