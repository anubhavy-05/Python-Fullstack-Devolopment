

# DICTIONARY IN PYTHON

A dictionary in Python is a data type used to store data in **key-value pairs**.
Each key is unique and is used to access its value.

## Why use a dictionary?

- Fast lookup by key
- Data can be updated easily
- Good for storing related information (like a student record)

## Basic syntax

```python
student = {
	"name": "Anubhav",
	"age": 20,
	"course": "Python"
}
```

## Important points

- Dictionary is written using `{}`
- Keys must be unique (value may change but keys are not)
- Keys are usually immutable types (string, int, tuple)
- Values can be any data type
- Dictionaries are mutable (you can add, update, delete items)
- index cocept is not in dict

## Access values

```python
print(student["name"])      # Anubhav
print(student.get("age"))   # 20
```

`get()` is safer because it does not give an error if the key is missing.

## Add or update values

```python
student["city"] = "Delhi"      # add new key-value pair
student["age"] = 21             # update existing value
```

## Remove values

```python
student.pop("course")           # removes key "course"
del student["city"]             # deletes key "city"
```

## Loop through dictionary

```python
for key, value in student.items():
	print(key, value)
```

## Dictionary methods (common)

- `keys()` -> returns all keys
- `values()` -> returns all values
- `items()` -> returns key-value pairs
- `get(key)` -> returns value of key safely
- `update()` -> merges another dictionary
- `pop(key)` -> removes and returns value of key

## Example with nested dictionary

```python
employees = {
	"emp1": {"name": "Ravi", "salary": 50000},
	"emp2": {"name": "Neha", "salary": 60000}
}

print(employees["emp1"]["name"])  # Ravi
```

## Summary

Dictionary is one of the most useful Python data structures.
Use it when you need to map one thing (key) to another thing (value).

