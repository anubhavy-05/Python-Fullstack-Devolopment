# "a built-in function that returns the length of an object" and it can store elements of different type(int, float, string, etc.) in a single list.

Marks=[90, 80, 70, 60, 50]

print("The marks are:", Marks)

print("The number of subjects is:", len(Marks))

print("The first mark is:", Marks[0])

print("The last mark is:", Marks[-1])   

  
                     #LIST METHODS


Marks=[90, 80, 70, 60, 50]

Marks.append(40) # To add an element at the end of the list.
print("The marks after appending 40 are:", Marks)  

Marks.sort() # To sort the list in ascending order.
print("The marks after sorting are:", Marks)

Marks.sort(reverse=True) # To sort the list in descending order.
print("The marks after sorting in descending order are:", Marks)

Marks.insert(2, 75) # To add an element at a specific index in the list.
print("The marks after inserting 75 at index 2 are:", Marks)

Marks.remove(60) # To remove an element from the list.
print("The marks after removing 60 are:", Marks)

Marks.pop(3) # To remove the last element from the list.
print("The marks after popping the element at index 3 are:", Marks)



                    # LIST SLICING


Marks=[90, 80, 70, 60, 50]
 # To find the minimum value in the list.

print("The first three marks are:", Marks[0:3]) # To get a sublist of the first three elements.

print("The last two marks are:", Marks[-2:]) # To get a sublist of the last two elements.

print("The marks from index 1 to 4 are:", Marks[1:5]) # To get a sublist of elements from index 1 to 4.



Marks=[90, 80, 70, 60, 50]

print("The minimum mark is:", min(Marks)) # To find the minimum value in the list.
print("The maximum mark is:", max(Marks)) # To find the maximum value in the list.