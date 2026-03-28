                       

                             # set 


s1 = {1, 2, 3, 4, 5}
print(s1) # Output: {1, 2, 3, 4, 5} (sets are unordered collections of unique elements)
print(type(s1)) # Output: <class 'set'> (s1  is a set)


s2 = {}
print(type(s2)) # Output: <class 'dict'> (s2 is an empty dictionary, not a set), to create an empty set, you should use s2 = set(),


s3 = set(10,21,23,45) # This will raise a TypeError because the set() constructor expects a single iterable argument, but you are passing multiple integers. To create a set with these values, you should pass them as a list or a tuple, like this: s3 = set([10, 21, 23, 45]) or s3 = set((10, 21, 23, 45)).




                            #excess set elements,in set there is no concept of indexing because sets are unordered collections, so you cannot access elements by their position. However, you can iterate over the elements of a set using a for loop or convert the set to a list to access elements by index. For example: x = {1, 2, 3, 4, 5}
for element in x:
    print(element) # This will print each element in the set x, but the order of the elements may not be the same as they were added to the set.    


s4 = {1, 2, 3, 4, 5, 5, 6, 7}
print(s4) # Output: {1, 2, 3, 4, 5, 6, 7} (the duplicate element 5 is automatically removed from the set),
