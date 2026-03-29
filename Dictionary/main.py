

        # DICTIONARY IN PYTHON,it is a collection of key-value pairs where each key is unique and maps to a specific value. Dictionaries are mutable, meaning you can change their contents after they are created. They are defined using curly braces {} and the key-value pairs are separated by commas. The keys and values can be of any data type, including strings, numbers, lists, and even other dictionaries.
# Here are some examples of dictionaries in Python:


# Example 1: A simple dictionary with string keys and integer values

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {"name": "Alice", "age": 30, "city": "New     York"}     

# Example 2: A dictionary with mixed data types

my_dict = {"name": "Bob", "age": 25, "hobbies": ["reading", "gaming", "hiking"], "is_student": True}
print(my_dict)  # Output: {"name": "Bob", "age": 25, "hobbies": ["reading", "gaming", "hiking"], "is_student": True}  


# Example 3: A nested dictionary

my_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(my_dict)  # Output: {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}




                     #ACCESSING AND MODIFYING DICTIONARIES



# You can access values in a dictionary using their corresponding keys. For example:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])  # Output: "Alice"
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: "New York"
print(my_dict.get("name"))  # Output: "Alice" (using the get method to access values)
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York']) (to get all values in the dictionary)
print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'city']) (to get all keys in the dictionary)




# You can also add, modify, or delete key-value pairs in a dictionary. For example:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

my_dict["age"] = 31  # Modifying the value of the "age" key
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
del my_dict["city"]  # Deleting the "city" key-value pair
print(my_dict)  # Output: {"name": "Alice", "age": 31, "email": "alice@example.com"}    

# Dictionaries are a fundamental data structure in Python and are widely used for various applications, such as storing and organizing data, implementing algorithms, and creating complex data structures. 



# Key Questions and Answers related to dictionary, IF we acess a key that is not in dictionar and we try to modify that like my_dict["gender"]=male then it will add a new key-value pair to the dictionary. If we try to access a key that is not in the dictionary without modifying it, it will raise a KeyError. For example, if we try to access my_dict["gender"] without assigning a value to it, it will raise a KeyError because the key "gender" does not exist in the dictionary. However, if we assign a value to the key "gender" like my_dict["gender"] = "male", it will add the key "gender" with the value "male" to the dictionary without raising an error.       

#example:1
my_dict = {"name": "Alice", "age": 30, "city": "New York"}  
print(my_dict["gender"]) # This will raise a KeyError because the key "gender" does not exist in the dictionary.  but if we do my_dict["gender"] = "male" then it will add the key "gender" with the value "male" to the dictionary without raising an error.     

    
    
