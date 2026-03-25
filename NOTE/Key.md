# Truncate :
truncation means that the decimal part is removed and only the whole number part is kept ie;

x=int(7.9)
print(x)

output  7


# Float() function :
 this function change any integer in decimal ie;

y=float(7)
print(y)
 
output 7.0 


# round() function :
 is a built-in function in Python that rounds a number to a specified number of decimal places. If the number of decimal places is not specified, it rounds to the nearest integer.rules of rounding: If the decimal part is less than 0.5, the number is rounded down. If the decimal part is 0.5 or greater, the number is rounded up.

z=round(7.8)
print(z) 
z=round(7.8, 1) # Rounds to 1 decimal place.
print(z)

 Output: 8

# Typecasting
age = 20
text = "Age: "
print(text + age)

A) Age:20
B)Error

output is:Error

in python we can't add a string and integer with + operator this is called type error for solving this we use (str()) ie;
print(text + str(age))

# comma ka use (in ptyhon comma give a space automatically)

print(text,age)

# f string (string ke andar hi variable daal dena,)

 print(f"{text}{age}")

 summary: in python "apple" + 5 = error hota hai lekin "apple" + "5 = apple5 hpta hai ie; if we use  f" string , then we can't use datatype for that 

# f string kya hai ( ye f se start hoti hai kyu ki aap string ke quatation marks se pahale ek chhota f likhate hai esake baad aap kisi bhi variable ko curly braces {} ke andar daal sakate hai )

Example:

age=20
name="Rahul"
print(f"Hello,{name}! Apaki age {age} saal hai.")

output: Hello, Rahul! apaki age 20 saal hai.

# why f-string better

f-strings Kyun Better Hain?

No Typecasting Required:
 Aapko str(age) likhne ki zaroorat nahi padti. Python apne aap integer ko string mein convert kar leta hai.
Clean Code:
 Plus + signs aur bahut saare commas , ka jhanjhat khatam ho jata hai.
Expressions:
 Aap {} ke andar choti-moti calculations bhi kar sakte hain.
print(f"Next year aap {age + 1} ke ho jayenge.")

Example:1

pi = 3.14159
print(f"Value: {pi:.2f}") # Output: 3.14 (sirf 2 decimal tak)
output:  3.14

example:2

salary = 50000
print(f"Salary: {salary:,}") # Output: 50,000 (comma lag jayega) 


Eample:3 
#WAP using f-string to Hii ! Mera name Anubhav hai aur mera lucky number 7 hai. Take the name and lucky number as input from the user.

name="Anubhav"
lucky_number=7
print(f"Hi! My name is {name} and my lucky number is {lucky_number}.")

                        #  OR


#WAP using f-string to Hii ! Mera name Anubhav hai aur mera lucky number 7 hai. Take the name and lucky number as input from the user.


name = input("Enter your name: ")
lucky_number = int(input("Enter your lucky number: "))
print(f"Hi! My name is {name} and my lucky number is {lucky_number}.")

# we can also calculate in f string 

a = 15
b = 25

# Bina kisi extra variable ke direct curly braces mein calculation
print(f"Jab hum {a} aur {b} ko jodte hain, toh total {a + b} aata hai.")

Isme kya hua?
{a} ne 15 print kiya.
{b} ne 25 print kiya.
{a + b} ne pehle calculation ki (15 + 25 = 40) aur phir result print kiya.

# QUESTION 7 EXPLAINATION

cars = ["BMW", "Tesla", "Toyota","Audi"]
for i in range(len(cars)):
    if cars[i].startswith("T"):
        cars.pop(i) 
print(cars) 


​Initial List: ["BMW", "Tesla", "Toyota", "Audi"] (Indices: 0, 1, 2, 3)
​Iteration 0 (i=0): cars[0] is "BMW". "T" se shuru nahi hota. Kuch nahi hua.
​Iteration 1 (i=1): cars[1] is "Tesla". Yeh "T" se shuru hota hai, toh cars.pop(1) execute hua.
​Result: "Tesla" list se bahar nikal gaya.
​Ab list aisi dikhti hai: ["BMW", "Toyota", "Audi"]
​The Catch (Index Shift): Jaise hi "Tesla" hat gaya, "Toyota" ab index 1 par aa gaya aur "Audi" index 2 par.
​Iteration 2 (i=2): Ab loop index 2 par check karega. Lekin naye list mein index 2 par "Audi" hai (kyunki Toyota peeche shift ho chuka hai).
​"Audi" "T" se shuru nahi hota. Kuch nahi hua.
​Loop End: range(len(cars)) shuruat mein 4 tha, toh loop wahi ruk jayega.

