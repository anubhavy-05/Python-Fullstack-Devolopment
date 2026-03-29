               
               #set

. set is class               
. set is mutable 
. set is not sequence
. set is iterable 
. indexing is not applicable
. set can not have duplicate values
. set does not gaurantee to store values in the order of insetion 
. slicing operator is not applicable 

#
s1 = {1, 2, 3, 4, 5}
print(s1) # Output: {1, 2, 3, 4, 5} (sets are unordered collections of unique elements)
print(type(s1)) # Output: <class 'set'> (s1  is a set)

#
s2 = {}
print(type(s2)) # Output: <class 'dict'> (s2 is an empty dictionary, not a set), to create an empty set, you should use s2 = set()

#

s3 = set(10,21,23,45)
here typeError occur becouse set expected at 1 orgument but here is 3 argument pass ie; s3=set(3)
s3 = set(10,21,23,45) # This will raise a TypeError because the set() constructor expects a single iterable argument, but you are passing multiple integers. To create a set with these values, you should pass them as a list or a tuple, like this: s3 = set([10, 21, 23, 45]) or s3 = set((10, 21, 23, 45)).


# 
in set duplicates are not allowed, if you try to add duplicate elements to a set, they will be automatically removed, and only unique elements will be stored in the set. 

ie;
s4 = {1, 2, 3, 4, 5, 5, 6, 7}
print(s4) # Output: {1, 2, 3, 4, 5, 6, 7} (the duplicate element 5 is automatically removed from the set),



# aceess the element of set  (s1+s2 , s1*s2   not supported )


in set there is no concept of indexing because sets are unordered collections, so you cannot access elements by their position. However, you can iterate over the elements of a set using a for loop or convert the set to a list to access elements by index. For example:
x = {1, 2, 3, 4, 5}
for element in x:
    print(element) # This will print each element in the set x, but the order of the elements may not be the same as they were added to the set.    


 #concatination and repetition of sets
s1 = {1, 2, 3}
s2 = {4, 5, 6}  
s3 = s1.union(s2) # To concatenate two sets, you can use the union() method or the | operator.
print(s3) # Output: {1, 2, 3, 4, 5, 6} (the union of s1 and s2) 

print(s1 | s2) # Output: {1, 2, 3, 4, 5, 6} (the union of s1 and s2 using the | operator)

print(s1 * 3) # This will raise a TypeError because sets do not support repetition using the * operator. The * operator is designed to work with sequences like lists and tuples, but it cannot be used with sets because sets are unordered collections of unique elements. If you want to create a new set that contains multiple copies of the same elements, you can use the union() method or the | operator to combine the set with itself multiple times, like this: s1.union(s1).union(s1) or s1 | s1 | s1 which will create a new set that contains three copies of each element in s1, but since sets do not allow duplicate elements, the resulting set will still only contain one copy of each element.

print(s1.union(s1).union(s1)) # Output: {1, 2, 3} (a new set that contains three copies of each element in s1, but since sets do not allow duplicate elements, the resulting set still only contains one copy of each element)

print(s1 | s1 | s1) # Output: {1, 2, 3} (a new set that contains three copies of each element in s1 using the | operator, but since sets do not allow duplicate elements, the resulting set still only contains one copy of each element)

print(s1+s2) # This will raise a TypeError because sets do not support concatenation using the + operator. The + operator is designed to work with sequences like lists and tuples, but it cannot be used with sets because sets are unordered collections of unique elements. If you want to create a new set that contains all the elements from both sets, you can use the union() method or the | operator, like this: s1.union(s2) or s1 | s2 which will create a new set that contains all the unique elements from both sets.   

#
concatenation and repetition of sets is not supported in Python because sets are unordered collections of unique elements, and they do not allow duplicate elements. Therefore, you cannot concatenate or repeat sets using the + or * operators. Instead, you can use the union() method or the | operator to combine sets, but this will not create duplicates in the resulting set.



# comparison of sets 

there are several comparison operators that can be used to compare sets in Python, including ==, !=, <, <=, >, and >=. These operators compare the elements of the sets and return a boolean value based on the comparison. For example:

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 == s2) # Output: False (sets are equal if they contain the same elements)

print(s1 != s2) # Output: True (sets are not equal if they do not contain the same elements)

print(s1 < s2) # Output: False (s1 is a proper subset of s2 if all elements of s1 are in s2 and s1 is not equal to s2)

print(s1 <= s2) # Output: False (s1 is a subset of s2 if all elements of s1 are in s2)

print(s1 > s2) # Output: False (s1 is a proper superset of s2 if all elements of s2 are in s1 and s1 is not equal to s2)

print(s1 >= s2) # Output: False (s1 is a superset of s2 if all elements of s2 are in s1)


# note

#
 sets are unordered collections of unique elements, so the order of the elements in a set does not matter when comparing sets. Therefore, the comparison operators will return the same result regardless of the order of the elements in the sets.
#
 For example, if we have s3 = {3, 2, 1}, then s1 == s3 will return True because both sets contain the same elements, even though they are in a different order. Similarly, s1 < s3 will return False because s1 is not a proper subset of s3, and s1 > s3 will also return False because s1 is not a proper superset of s3.
#
 In summary, when comparing sets in Python, the order of the elements does not affect the comparison results, and the comparison operators will return the same result regardless of the order of the elements in the sets.



#  set object methods,in Python
sets have several built-in methods that allow you to perform various operations on sets. Here are some commonly used set methods: thier working is explained in the comments of the code below.
# add() 
method is used to add an element to a set. If the element already exists in the set, it will not be added again since sets do not allow duplicate elements.
# remove() 
method is used to remove a specific element from a set. If the element does not exist in the set, it will raise a KeyError.
# discard() 
method is used to remove a specific element from a set. If the element does not exist in the set, it will not raise an error and will simply do nothing.
# pop()
 method is used to remove and return an arbitrary element from a set. Since sets are unordered, there is no guarantee which element will be removed when using pop().
# clear() 
method is used to remove all elements from a set, resulting in an empty set.
# union()
method is used to return a new set that contains all the unique elements from both sets. It can also be used with the | operator.
# intersection() 
method is used to return a new set that contains only the elements that are present in both sets. It can also be used with the & operator.
#mdifference()
method is used to return a new set that contains the elements that are present in the first set but not in the second set. It can also be used with the - operator.
# symmetric_difference() 
method is used to return a new set that contains the elements that are present in either set but not in both sets. It can also be used with the ^ operator. 

# example

s1 = {1, 2, 3, 4, 5}

s1.add(6) # To add an element to the set s1.

print(s1) # Output: {1, 2, 3, 4, 5, 6} (the set s1 after adding the element 6) but since sets do not allow duplicate elements, if you try to add an element that already exists in the set, it will not be added again. For example, if you try to add 3 to s1 again using s1.add(3), the set will remain unchanged as {1, 2, 3, 4, 5, 6} because 3 is already an element of the set.,order of elements in a set is not guaranteed, so the output may not be in the same order as the input.it takes any order of the elements in the set when printing.

print(s1.remove(3)) # To remove the element 3 from the set s1. This will raise a KeyError if 3 is not in the set.

print(s1) # Output: {1, 2, 4, 5, 6} (the set s1 after removing the element 3)

print(s1.discard(4)) # To remove the element 4 from the set s1. This will not raise an error if 4 is not in the set.

print(s1) # Output: {1, 2, 5, 6} (the set s1 after discarding the element 4)

print(s1.pop()) # To remove and return an arbitrary element from the set s1. 

print(s1) # Output: {2, 5, 6} (the set s1 after popping an arbitrary element, but since sets are unordered, there is no guarantee which element will be removed when using pop())

print(s1.clear()) # To remove all elements from the set s1.

print(s1) # Output: set() (the set s1 after clearing all elements, resulting in an empty set)

# NOTE

# EXAMPLE:2

s2 = {5, 6, 7, 8, 9, 10}
s2.update(18) #  This will raise a TypeError because the update() method expects an iterable argument, but you are passing a single integer. To add a single element to the set using the update() method, you can pass it as a set or a list, like this: s2.update({18}) or s2.update([18]) which will add the element 18 to the set s2.


# NOTE 2

s1 = {1, 2, 3, 4, 5}
s1.add((6, 7)) # To add a tuple as an element to the set s1. This will work because tuples are immutable and can be added to a set, but the entire tuple will be treated as a single element in the set. So, after adding the tuple (6, 7) to s1, the set will contain the elements {1, 2, 3, 4, 5, (6, 7)}. However, if you try to add a list or another set as an element to the set s1 using s1.add([8, 9]) or s1.add({10, 11}), it will raise a TypeError because lists and sets are mutable and cannot be added to a set as elements.


s1.update((8, 9)) # To add multiple elements to the set s1 using the update() method with a tuple. This will work because the update() method can take any iterable as an argument, and it will add each element of the iterable to the set. So, after updating s1 with the tuple (8, 9), the set will contain the elements {1, 2, 3, 4, 5, (6, 7), 8, 9}. However, if you try to update the set s1 with a list or another set using s1.update([10, 11]) or s1.update({12, 13}), it will work because the update() method can take any iterable as an argument, and it will add each element of the iterable to the set. So, after updating s1 with the list [10, 11] or the set {12, 13}, the set will contain the elements {1, 2, 3, 4, 5, (6, 7), 8, 9, 10, 11} or {1, 2, 3, 4, 5, (6, 7), 8, 9, 12, 13} respectively.  

# What is difference between remove and discard in set


s2 = {5, 6, 7, 8, 9, 10}
print(s2.remove(7)) # To remove the element 7 from the set s2. This will raise a KeyError if 7 is not in the set.
print(s2) # Output: {5, 6, 8, 9, 10, 11} (the set s2 after removing the element 7)
print(s2.discard(8)) # To remove the element 8 from the set s2. This will not raise an error if 8 is not in the set.