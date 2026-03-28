               
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



# aceess the element of set

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