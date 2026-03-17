a=10
b=20    
print("Before swapping: a =", a, "b =", b)  # Print the values of a and b before swapping.
a=a+b  # Update a to be the sum of a and b.
b=a-b  # Update b to be the difference of the new a and the original b.
a=a-b  # Update a to be the difference of the new a and the new b.
print("After swapping: a =", a, "b =", b)