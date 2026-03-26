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


1.​Initial List: ["BMW", "Tesla", "Toyota", "Audi"] (Indices: 0, 1, 2, 3)
2.​Iteration 0 (i=0): cars[0] is "BMW". "T" se shuru nahi hota. Kuch nahi hua.
3.​Iteration 1 (i=1): cars[1] is "Tesla". Yeh "T" se shuru hota hai, toh cars.pop(1) execute hua.
​Result: "Tesla" list se bahar nikal gaya.
​Ab list aisi dikhti hai: ["BMW", "Toyota", "Audi"]
4.​The Catch (Index Shift): Jaise hi "Tesla" hat gaya, "Toyota" ab index 1 par aa gaya aur "Audi" index 2 par.
5.​Iteration 2 (i=2): Ab loop index 2 par check karega. Lekin naye list mein index 2 par "Audi" hai (kyunki Toyota peeche shift ho chuka hai).
​"Audi" "T" se shuru nahi hota. Kuch nahi hua.
6.​Loop End: range(len(cars)) shuruat mein 4 tha, toh loop wahi ruk jayega.

# QUESTION 10

a=[1, 2, 3]
b=[1, 2, 3]
print(a==b) # Output: True (the contents of the lists are the same)
print(a is b) # Output: False (a and b are different objects in memory)

# == (Equality Operator)
1.Ye sirf Value check karta hai.
Aapne a mein [1,2,3] rakha aur b mein bhi [1,2,3].
Kyunki dono lists ke andar ka data bilkul same hai, isliye a == b ka result True aaya.
Sochiye: Do alag-alag ghar hain, lekin dono ka design ek jaisa hai.
#  is (Identity Operator)
2.Ye Memory Address (Object Identity) check karta hai.
Jab aap a = [1,2,3] likhte hain, Python memory mein ek jagah (Object) banata hai.
Jab aap b = [1,2,3] likhte hain, Python memory mein ek doosri alag jagah banata hai, bhale hi data same ho.
Kyunki a aur b do alag objects ko point kar rahe hain, isliye a is b ka result False aaya.
Sochiye: Do alag-alag ghar hain. Design same ho sakta hai, lekin unka address (Location) alag hai.
Ek Interesting Twist (Anubhav, dhyan se dekhna!)
Agar aap code ko thoda badal dein:

a = [1,2,3]
b = a         # Yahan humne b ko a ka reference de diya
print(a is b)

Ab output True aayega! Kyunki ab b koi naya object nahi hai, balki wo usi memory location ko point kar raha hai jahan a hai.


# QUESTION 11

x="10"
if x==10:
    print("A")   
else:
    print(x*2)


1. Pehla Step: Comparison (if x == 10)

Yahan par x ki value hai "10" (dhayan dijiye, yeh quotes mein hai, matlab yeh ek String hai).
Lekin hum ise compare kar rahe hain 10 se (jo ek Integer hai).
Python mein ek String aur ek Integer kabhi bhi barabar (equal) nahi ho sakte, bhale hi unka chehra ek jaisa dikhe.
Isliye x == 10 ka result False aayega aur code else block mein chala jayega.


# QUESTION 15



Chalo is trick question ka logic step-by-step samajhte hain:

Yahan x = [] (ek empty list) hai. Python mein in conditions ko aise evaluate kiya jata hai:

if x == False:
Halanki empty list ek "Falsy" value hoti hai, par wo exact boolean False ke barabar (==) nahi hoti. Ek list aur ek boolean alag-alag data types hain. Isliye yeh condition False ho jayegi aur code aage badh jayega.

elif x is False:
is operator memory identity (kya dono exactly same object hain?) check karta hai. Ek list aur ek boolean value memory mein alag-alag objects hote hain. Isliye yeh condition bhi False ho jayegi.

elif not x:
Yahan aakar game change hota hai! not operator variable ki "truthiness" check karta hai. Python mein empty list [] ko Falsy mana jata hai. Toh jab hum not x likhte hain, toh wo not False jaisa behave karta hai, jo ki True ban jata hai. Yeh condition satisfy ho gayi!

Result:
Condition match hone par "Spider-Man" print ho jayega aur uske aage ka else block ignore ho jayega.


# QUESTION 16

Chalo is trick ka logic samajhte hain, jo Python ke memory management par based hai:

Logic Explanation
List Creation (x = [1, 2, 3]): Yahan memory mein ek list object create hota hai jisme [1, 2, 3] store hota hai, aur variable x us object ko point karne lagta hai.

Reference Assignment (y = x): Yeh is code ka sabse crucial step hai! Python mein jab hum list ko aise assign karte hain, toh ek nayi list nahi banti. Balki, y bhi usi same memory location (usi same list) ko point karne lagta hai jise x kar raha hai. Is concept ko Aliasing kehte hain.

Modification (y.append(4)): Jab hum y mein 4 append karte hain, toh wo original list mein jaakar add ho jata hai. Kyunki x aur y dono ek hi list se jude hain, wo list ab [1, 2, 3, 4] ban chuki hai.

Final Output (print(x)): Jab hum x ko print karte hain, toh wo usi updated list ko dikhata hai, isliye output [1, 2, 3, 4] aata hai.

Quick Tip:
Agar aap chahte the ki y ek bilkul alag list bane aur usme change karne par x par koi asar na pade, toh aapko copy banani padti. Jaise ki:

y = x.copy() ya

y = x[:] (Slicing method)

# QUESTION 17


Gemini said
Sahi answer hai B) False.

Dekhne mein yeh thoda ajeeb lag sakta hai ki 0.1 + 0.2 exact 0.3 kyun nahi hai, par iske peeche ek classic computer science concept hai jise Floating-Point Precision kehte hain.

Logic Explanation

1. Binary Representation: Hum numbers ko base-10 (decimal) mein sochte hain, par computers unhe base-2 (binary) mein store karte hain. Jaise fraction 1/3 ko decimal mein exact likhna mushkil hai (0.3333...), bilkul waise hi decimals 0.1 aur 0.2 ko binary mein exact represent nahi kiya ja sakta; unka binary fraction infinitely repeat hota hai.

2. Approximation: Kyunki exact representation possible nahi hai, Python (aur IEEE 754 standard follow karne wali lagbhag saari programming languages) in numbers ko ek bohot hi close approximate value ke roop mein round off karke store karti hain.

3. The Addition: Jab Python memory mein 0.1 aur 0.2 ke approximate binary equivalents ko add karta hai, toh us addition ka actual internal result 0.3 nahi banta. Wo kuch is tarah nikal kar aata hai:
0.1 + 0.2 = 0.30000000000000004

4. Equality Check (==): Ab jab interpreter evaluate karta hai ki kya 0.30000000000000004 == 0.3, toh dono values perfectly match nahi karti. Isliye output False aata hai.