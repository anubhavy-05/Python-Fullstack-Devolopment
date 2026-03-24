

                        # Slicing in Python


# Slicing is a powerful feature in Python that allows you to extract a portion of a sequence (like a list, string, or tuple) by specifying a range of indices. The syntax for slicing is as follows:
# sequence[start:stop:step]
# - `start`: The index where the slice starts (inclusive). If omitted, it defaults to 0.
# - `stop`: The index where the slice ends (exclusive). If omitted, it defaults to the length of the sequence.
# - `step`: The step size or the interval between indices. If omitted, it defaults to 1.
# Here are some examples of slicing:
#strobject[start:stop:step]



# Example 1: Slicing a list

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
print(my_list[2:5])  # Output: [2, 3, 4]
print(my_list[:4])   # Output: [0, 1, 2, 3]
print(my_list[5:])   # Output: [5, 6, 7, 8, 9]
print(my_list[::2])  # Output: [0, 2, 4, 6, 8]
print(my_list[1:8:3]) # Output: [1, 4, 7]  
print(my_list[8:1:-3]) # Output: [8, 5, 2]

# Example 2: Slicing a string

my_string = "Hello, World!"
print(my_string[0:5])  # Output: "Hello"    
print(my_string[7:])   # Output: "World!"
print(my_string[::2])  # Output: "Hlo ol!"
print(my_string[1:10:3]) # Output: "el,W"

# Example 3: Slicing a tuple

my_tuple = (10, 20, 30, 40, 50) 
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[2:])   # Output: (30, 40, 50)
print(my_tuple[::2])  # Output: (10, 30, 50)
print(my_tuple[1:5:2]) # Output: (20, 40)

# Slicing is a versatile tool that can be used for various purposes, such as extracting specific elements, reversing sequences, or creating sublists. It is an essential part of Python programming and can help you manipulate data efficiently.
