

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
