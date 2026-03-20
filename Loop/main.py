i=1 
while i<=5:
    print(i)
    i+=1    
#WAP to print hello five times using while loop.
i=1 
while i<=5:
    print("Hello")
    i+=1    

#WAP TO PRINT 100 TO 1 IN REVERSE ORDER USING WHILE LOOP.
i=100       
while i>=1:
    print(i)
    i-=1      

#WAP to take a number from user and print its multiplication table using while loop.
X=int(input("enter the number:"))
i=1
while i<=10:
    print(X*i)
    i+=1

#WAP to print the squares of first 10 natural numbers using while loop.
i=1
while i<=10:
    print(i**2)
    i+=1

 #WAP to print the sum of first n natural numbers using while loop. 

x=int(input("Enter "))
i=1
sum=0
while i<=x:
    sum+=i
    i+=1
print(sum)  

#WAP to print the sum of first n natural numbers using for loop.

x=int(input("Enter "))
sum=0
for i in range(1, x+1):
    sum+=i
print(sum)

#WAP to print the multiplication table of a number using for loop.

x = int(input("Enter "))
for i in range(1, 11):
    print(x * i)


#WAP to print the squares of first 10 natural numbers using for loop.

n=5
sum=0
for i in range(1, n+1):
    sum+=i      
print(sum)  

#WAP to print the sum of first n natural numbers using while loop.

n=10
sum=0
i=1
while i<=n: 
    sum+=i      
    i+=1
print(sum)



sahi_password = "python123"
password = input("enter the password:")
while password != sahi_password:
    print("wrong password, try again")
    password = input("enter the password:")
print("correct password, welcome to the system")

    
