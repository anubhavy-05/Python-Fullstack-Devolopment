
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




for i in range(1, 21):
    if i%2==0:
        print(i)



charge = [50, 25, 25]  # Create a s of charges.
refund = sum(charge[:2])  # Add first two charges: 50 + 25 = 75.
charge.remove(25)  # Remove the first occurrence of 25 from the s.
print(sum(charge) - refund)  # Print remaining total minus refund amount.


#WAP using f-string to Hii ! Mera name Anubhav hai aur mera lucky number 7 hai. Take the name and lucky number as input from the user.

name="Anubhav"
lucky_number=7
print(f"Hi! My name is {name} and my lucky number is {lucky_number}.")

                        #  OR

#WAP using f-string to Hii ! Mera name Anubhav hai aur mera lucky number 7 hai. Take the name and lucky number as input from the user.

name = input("Enter your name: ")
lucky_number = int(input("Enter your lucky number: "))
print(f"Hi! My name is {name} and my lucky number is {lucky_number}.")













# wap to print twinkle twikle little star poem i  python using print statement.

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

#wap to print the table of a number using while loop. Take the number as input from the user.

number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
# OR wap to print the table of a number using for loop. Take the number as input from the user.
    
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# WAP to print the table of a number using for loop. Take the number as input from the user.

    number = int(input("Enter a number: "))
    n = 10
    for i in range(1, n + 1):   
        print(f"{number} x {i} = {number * i}")  


# WAP to print the sum of two numbers using for loop. Take the two numbers as input from the user.


a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
sum=a+b
print("sum of two number is:", sum)
print(f"The sum of {a} and {b} is: {sum}")


#WAP to print the remainder of two numbers . Take the two numbers as input from the user.


a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
remainder=a%b
print("The remainder of the division is:", remainder)
print(f"The remainder of {a} divided by {b} is: {remainder}")



a=int(input("Enter a number: "))
z=int(input("Enter a number: "))
remainder=a%z
print(f"The remainder of {a} divided by {z} is: {remainder}")
print("The remainder divided by z  is:", remainder)




a=int(input("Enter a number: "))
square=a**2
print("The square of the number is:", square)
print(f"The square of {a} is: {square}")


# 50,60,80,90 print max and min number from the s using max() and min() function.
numbers = [50, 60, 80, 90]
print("Maximum number in the s is:", max(numbers))
print("Minimum number in the s is:", min(numbers))



#WAP to store 7 fruits in a s take the input from the user and print the s of fruits.
fruits = []
f1 = input("Enter the name of fruit 1: ")
fruits.add(f1)
f2 = input("Enter the name of fruit 2: ")
fruits.add(f2)
f3 = input("Enter the name of fruit 3: ")
fruits.add(f3)
f4 = input("Enter the name of fruit 4: ")
fruits.add(f4)
f5 = input("Enter the name of fruit 5: ")
fruits.add(f5)
f6 = input("Enter the name of fruit 6: ")   
fruits.add(f6)
f7 = input("Enter the name of fruit 7: ")
fruits.add(f7)

print("The s of fruits is:", fruits)


# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "madad": "help",
    "pyaar": "love",
    "dost": "friend",
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "हाँ": "Yes",
    "नहीं": "No"
}
word = input("Enter a Hindi word to look up its English translation: ")
print(words[word])



#WAP to input eight numbers from the user and store them in a s. Then, print the s of numbers.(once)

s=set()
l1 = int(input("Enter number 1: "))
s.add(l1)
l2 = int(input("Enter number 2: "))
s.add(l2)
l3 = int(input("Enter number 3: "))
s.add(l3)
l4 = int(input("Enter number 4: "))
s.add(l4)
l5 = int(input("Enter number 5: "))
s.add(l5)
l6 = int(input("Enter number 6: "))
s.add(l6)
l7 = int(input("Enter number 7: "))
s.add(l7)
l8 = int(input("Enter number 8: "))
s.add(l8)

print("The s of numbers is:", s)


#create an empty dictionary to allow four friends to enter their names and phone numbers. Then, print the dictionary.


friends = {}
f1 = input("Enter the name of friend 1: ")
p1 = input("Enter the phone number of friend 1: ")
friends.update({f1: p1})

f2 = input("Enter the name of friend 2: ")
p2 = input("Enter the phone number of friend 2: ")
friends.update({f2: p2})

f3 = input("Enter the name of friend 3: ")
p3 = input("Enter the phone number of friend 3: ")
friends.update({f3: p3})

f4 = input("Enter the name of friend 4: ")
p4 = input("Enter the phone number of friend 4: ")
friends.update({f4: p4})

print("The dictionary of friends is:", friends)


#WAP to to print a massage byn usin if and elif ladder. Take the age as input from the user.

age=int(input("Enter your age: "))
if age<18:
    print("You are a minor.")
elif age>=18 and age<65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

    #WAP to print yes if the enter by the usre is less than or equal to 18. Take the age as input from the user.

age=int(input("Enter your age: "))
if age<=18:
    print("Yes.")
else:
    print("No.")  