                       

                             # set 


s1 = {1, 2, 3, 4, 5}
print(s1) # Output: {1, 2, 3, 4, 5} (sets are unordered collections of unique elements)
print(type(s1)) # Output: <class 'set'> (s1  is a set)


s2 = {}
print(type(s2)) # Output: <class 'dict'> (s2 is an empty dictionary, not a set), to create an empty set, you should use s2 = set(),


s3 = set(10,21,23,45) # This will raise a TypeError because the set() constructor expects a single iterable argument, but you are passing multiple integers. To create a set with these values, you should pass them as a list or a tuple, like this: s3 = set([10, 21, 23, 45]) or s3 = set((10, 21, 23, 45)).




                      #excess set elements,
                      
    # in set there is no concept of indexing because sets are unordered collections, so you cannot access elements by their position. However, you can iterate over the elements of a set using a for loop or convert the set to a list to access elements by index. For example: 


x = {1, 2, 3, 4, 5}
for element in x:
    print(element) # This will print each element in the set x, but the order of the elements may not be the same as they were added to the set.    

# Example:2
x = {1, 2, 3, 4, 5}
for i in x:
    print(i) # This will print each element in the set x, but the order of the elements may not be the same as they were added to the set.


                 #built-in functions of set

# EXAMPLE:1

s1 = {1, 2, 3, 4, 5}
print(len(s1)) # Output: 5 (the number of elements in the set)
print(max(s1)) # Output: 5 (the largest element in the set)
print(min(s1)) # Output: 1 (the smallest element in the set)
print(sum(s1)) # Output: 15 (the sum of all elements in the set)
print(sorted(s1)) # Output: [1, 2, 3, 4, 5] (a sorted list of the elements in the set)
print(set(reversed(s1))) # Output: {5, 4, 3, 2, 1} (a set with the elements in reverse order, but since sets are unordered, the output may not be in the same order as the input)   


# EXAMPLE:2

s2={"apple", "banana", "cherry", "date", "fig"}
print(len(s2)) # Output: 5 (the number of elements in the set)
print(max(s2)) # Output: "fig" (the largest element in the set based on alphabetical order)
print(min(s2)) # Output: "apple" (the smallest element in the set based on alphabetical order)
print(sum(s2)) # This will raise a TypeError because the sum() function cannot be applied to a set of strings. The sum() function is designed to work with numeric data types, and it cannot be used to concatenate strings or perform any other operation on non-numeric data. If you want to concatenate the strings in the set, you can use the join() method instead, like this: "".join(s2) which will concatenate all the strings in the set into a single string.
print(sorted(s2)) # Output: ['apple', 'banana', 'cherry', 'date', 'fig'] (a sorted list of the elements in the set based on alphabetical order)
print(set(reversed(s2))) # Output: {'fig', 'date', 'cherry', 'banana', 'apple'} (a set with the elements in reverse order, but since sets are unordered, the output may not be in the same order as the input)