
#WAP to take a number from user and check whether it is positive or non-positive only using if statement.
x=int(input("enter the number:"))
if x>=0:
    print("the number is positive")
if x<0:
    print("the number is non-positive")


#WAP to take a number from user and check whether it is positive or non-positive using if-else statement.

x=int(input("enter the number:"))
if x>=0:
    print("the number is positive")
else:
    print("the number is non-positive")

#WAP to take a number from user and check whether it is positive or non-positive using if-elif-else statement.


x=int(input("enter the number:"))   
if x>0:
    print("the number is positive")
elif x<0:
    print("the number is non-positive")             
else:
    print("the number is zero which is neither positive nor negative")   



x=int(input("enter the number:")) 
if x>18:
    print("you are eligible to vote")   
else:
    print("you are not eligible to vote")    

#WAP to take a score from user and print the grade according to the following criteria:
#Score >= 80: "Excellent"
#Score >= 50 and < 80: "Very Good"
#Score >= 70: "Good"


score=int(input("enter the score:"))
if score>=80:
    print("Excellent")
elif score>=50 and score <80:
    print("very good")
elif score>=70:
    print("good")
else:
    print("keep trying")

#WAP to check whether the number is three digit number or not.
x=int(input("enter the number:"))
if x>=100 and x<=999:
    print("the number is a three-digit number")
else:
    print("the number is not a three-digit number")


#WAP to take a year from user and check whether it is a leap year or not.

x=int(input("enter the number:"))
if x%4==0:
    print("the year is a leap year ")
else:
    print("the year is not a leap year")

#WAP to take a price of crop from user and give the suggestion to the farmer according to the following criteria:
#Price > 5000: "Good time to sell"
#Price >= 3000 and <= 5000: "Average price, you can hold"
#Price < 3000: "Market is down, hold the crop"

x=int(input("enter the number:"))
if x>5000:
    print("good time to sell")
elif x>=3000 and x<=5000:
    print("Average price,you can hold ")
elif  x<3000: 
    print("market is down, hold the crop")
else:
    print("invalid price")
