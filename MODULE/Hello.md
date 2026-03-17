# Hello.py - Line by Line Explanation

## Line 1: Comment
```python
# Import the built-in 'keyword' module which contains information about Python's reserved keywords
```
- This is a **comment line** (starts with `#`)
- It explains what the next line of code does
- Comments are ignored by Python and are only for human readability
- This comment describes that we will import the `keyword` module

## Line 2: Import Statement
```python
import keyword
```
- **`import`** is a Python keyword that loads modules
- **`keyword`** is a built-in module in Python
- This module provides tools to access Python's reserved keywords information
- After importing, we can use `keyword.kwlist` to access all reserved keywords
- **Purpose:** Access Python's reserved keywords list

## Line 3: Empty Line
```python

```
- This is a blank line
- Used for code readability and organization
- Python ignores blank lines

## Line 4: Comment
```python
# Access the 'kwlist' attribute from the keyword module which contains all reserved keywords and print them
```
- Another **comment line** explaining the next code
- Describes that we will access the `kwlist` attribute (property) from the `keyword` module
- `kwlist` contains all reserved keywords that cannot be used as variable names

## Line 5: Print Keywords
```python
print(keyword.kwlist) # kwlist is a list of all reserved words that cannot be used as variable names in Python
```
- **`print()`** is a built-in Python function that displays output to the console
- **`keyword.kwlist`** accesses the list of all reserved keywords from the keyword module
- **Inline comment** at the end explains what `kwlist` is
- **Output Example:** `['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', ...]`

## Line 6: Print Keyword Count
```python
print("total number of keywords in python",len(keyword.kwlist))# Print the total number of reserved keywords in Python by calculating the length of the kwlist
```
- **`print()`** displays the message along with the keyword count
- **`"total number of keywords in python"`** is a string message (text in quotes)
- **`len(keyword.kwlist)`** calculates the total count of keywords in the list
  - `len()` function returns the length (number of items) in a list
- **Inline comment** explains this line's purpose
- **Output Example:** `total number of keywords in python 35`

---

## Summary

| Line | Purpose |
|------|---------|
| 1 | Comment explaining the import |
| 2 | Import the keyword module |
| 3 | Blank line for readability |
| 4 | Comment explaining the next action |
| 5 | Print all reserved keywords to console |
| 6 | Print the total count of keywords |

**Overall Goal:** Display all Python's reserved keywords and count how many there are (currently 35 keywords in Python 3.x)
