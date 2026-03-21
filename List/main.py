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

print("The index of mark 80 is:", Marks.index(80)) # To find the index of a specific element in the list.


Marks=[90, 80, 70, 60, 50]

print(sum(Marks)) # To find the sum of all the elements in the list.
print("The minimum mark is:", min(Marks)) # To find the minimum value in the list.
print("The maximum mark is:", max(Marks)) # To find the maximum value in the list.


Marks=[90, 80, 70, 60, 70, 50, 70]
print("the count of mark 70 is:", Marks.count(70)) # To count the number of occurrences of a specific element in the list.
print("the index of the first occurrence of mark 70 is:", Marks.index(70)) # To find the index of the first occurrence of a specific element in the list.



                    # LIST SLICING


Marks=[90, 80, 70, 60, 50]
 # To find the minimum value in the list.

print("The first three marks are:", Marks[0:3]) # To get a sublist of the first three elements.

print("The last two marks are:", Marks[-2:]) # To get a sublist of the last two elements.

print("The marks from index 1 to 4 are:", Marks[1:5]) # To get a sublist of elements from index 1 to 4.

            
             #REPITITION OPERATOR

#(when we multiply 3*4 we get 12  becouse both are integers but when we multiply a list by an integer it repeats the elements of the list that many times.  ie; [1, 2] * 3 will give [1, 2, 1, 2, 1, 2] because the list [1, 2] is repeated three times.)             

Marks=[90, 80, 70, 60, 50]

print("The marks are:", Marks)

print("The marks repeated twice are:", Marks * 2) # To repeat the elements of the list.


                #LIST COMPREHENSION
#(List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.)

Marks=[90, 80, 70, 60, 50]
squared_marks=[mark**2 for mark in Marks] # To create a new list of squared marks using list comprehension.
print("The squared marks are:", squared_marks)


                    #LIST IN LIST


Marks=([[90, 80], [70, 60], [50, 40]]) # A list of lists, where each inner list represents a group of marks.
print("The marks are:", Marks)
print("The first group of marks is:", Marks[0]) 
print("The second mark of the first group is:", Marks[0][1]) # To access the second mark of the first group.


i=1
while i!=0:
    print(i)
    i+=1