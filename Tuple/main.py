

                     # Tuple in Python

# A tuple is an ordered, immutable collection of items in Python. It is similar to a list, but unlike lists, tuples cannot be modified after they are created. Tuples are defined using parentheses () and can contain elements of different data types.    
# Here are some examples of tuples in Python:

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)  # Output: ("apple", "banana", "cherry")

my_tuple = (1, "hello", 3.14)
print(my_tuple)  # Output: (1, "hello", 3.14)

# You can access elements in a tuple using indexing, just like with lists:

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30
print(my_tuple[-1]) # Output: 50    

# However, since tuples are immutable, you cannot modify their elements after they have been created. For example, the following code will raise an error:
my_tuple = (1, 2, 3)

# my_tuple[0] = 10  # This will raise a TypeError
# Tuples are often used to group related data together, especially when the data should not be modified. They can also be used as keys in dictionaries or as elements of sets, which is not possible with lists due to their mutability.        


          #note
    
t1=()
print(type(t1)) # Output: <class 'tuple'> (t1 is an empty tuple)

t2=[]
print(type(t2)) # Output: <class 'list'> (t2 is an empty list)

t4=(6)
print(type(t4)) # Output: <class 'int'> (t4 is not a tuple, it's just an integer)

t5=(6,)
print(type(t5)) # Output: <class 'tuple'> (t5 is a tuple)

t6=[6,7,8]
print(type(t6)) # Output: <class 'list'> (t6 is a list)

t7=(6,7,8,)
print(type(t7)) # Output: <class 'tuple'> (t7 is a tuple , the trailing comma does not affect the type)

t8=6,8,4,9
print(type(t8)) # Output: <class 'tuple'> (t8 is a tuple, parentheses are optional when defining a tuple with multiple elements)

t9=6,8,4,9,
print(type(t9)) # Output: <class 'tuple'> (t9 is a tuple, the trailing comma does not affect the type)



                             # Key Questions and Answers related to range 

# Example 1

r=range(10,20,1)
print(r[0]) # Output: 10 (accessing the first element of the range)
print(r[5]) # Output: 15 (accessing the sixth element of the range)
print(r[-1]) # Output: 19 (accessing the last element of the range)
print(len(r)) # Output: 10 (the range contains 10 elements: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

# Example 2

r2 = range(5)
print(list(r2))     # Output: [0, 1, 2, 3, 4] (converting the range to a list to see its elements)

# EXAMPLE 3

t1=(10,5,20,15)
i=0
while i<len(t1):
    print(t1[i]) # Output: 10, 5, 20, 15 (printing each element of the tuple)
    i+=1

# EXAMPLE 4

t1=(10,5,20,15)
for i in t1:
    print(i) # Output: 10, 5, 20, 15 (printing each element of the tuple using a for loop)



                   #built-in functions related to tuple

# Example 1

t1=(10,5,20,15)
print(len(t1)) # Output: 4 (the tuple contains 4 elements)
print(max(t1)) # Output: 20 (the largest element in the tuple)
print(min(t1)) # Output: 5 (the smallest element in the tuple)
print(sum(t1)) # Output: 50 (the sum of all elements in the tuple)
print(sorted(t1)) # Output: [5, 10, 15, 20] (a sorted list of the elements in the tuple)
print (tuple(reversed(t1))) # Output: (15, 20, 5, 10) (a tuple with the elements in reverse order)


                  #concatination and repetition of tuples


# EXAMPLE 1  
               
t2=(1,2,3)
t3=(4,5,6)
t4=t2+t3
print(t4) # Output: (1, 2, 3, 4, 5, 6) (concatenating two tuples)

# EXAMPLE 2

t5=(1,2,3)
t6=t5*3
print(t6) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3) (repeating a tuple)

                       
                       #TUPLE OBJECT METHODS


t1=(10,5,20,15)
print(t1.index(20)) # Output: 2 (the index of the first occurrence of 20 in the tuple)
print(t1.index(5))  # Output: 1 (the index of the first occurrence of 5 in the tuple)
# print(t1.index(25)) # This will raise a ValueError because 25 is  not in the tuple        
print(t1.count(10)) # Output: 1 (the number of times 10 appears in the tuple)
print(t1.count(5))  # Output: 1 (the number of times    5 appears in the tuple)
print(t1.count(25)) # Output: 0 (the number of times 25 appears in the tuple)                           
   

                        #slicing operator in tuples , t1[start:stop:step]

t1=(10,5,20,15,25,30,35)
print(t1[2:5])  # Output: (20, 15, 25) (elements from index 2 to 4)
print(t1[:3])   # Output: (10, 5, 20) (elements from the beginning to index 2)
print(t1[3:7])  # Output: (15, 25, 30, 35) (elements from index 3 to 6)
print(t1[::2])  # Output: (10, 20, 25, 35) (every second element)
print(t1[::-1]) # Output: (35, 30, 25, 15, 20, 5, 10) (all elements in reverse order)



                     #input from user in tuples

name = input("Enter your name: ")
age = int(input("Enter your age: "))
person = (name, age)
print("Person:", person) # Output: Person: ('Alice', 30) (assuming the user entered "Alice" and 30) 

