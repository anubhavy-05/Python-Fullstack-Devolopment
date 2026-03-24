# Python Strings - Complete Notes from Scratch

This file explains every string topic used in your `main.py` in a clear, beginner-friendly way.

## 1) What Is a String?

A **string** is a sequence of characters written inside quotes.

Examples:

```python
s1 = "hello"
s2 = 'python'
```

- Strings are ordered (each character has a position/index).
- Strings are immutable (you cannot change a character directly).

---

## 2) Printing a String and Accessing Characters (Indexing)

```python
S1 = "mysirg"
print(S1)
print(S1[0])
print(S1[2])
print(S1[-1])
```

### Index rules

- Positive index starts from left, beginning at `0`.
- Negative index starts from right, beginning at `-1`.

For `S1 = "mysirg"`:

- `S1[0]` -> `m`
- `S1[2]` -> `s`
- `S1[-1]` -> `g`

If index is out of range, Python gives `IndexError`.

---

## 3) Slicing (Getting Part of a String)

```python
print(S1[0:3])
print(S1[2:5])
```

General form:

```python
string[start:end]
```

- `start` is included.
- `end` is excluded.

So:

- `S1[0:3]` -> characters at index `0,1,2` -> `mys`
- `S1[2:5]` -> characters at index `2,3,4` -> `sir`

Useful shortcuts:

- `S1[:3]` -> from beginning to index `2`
- `S1[2:]` -> from index `2` to end
- `S1[:]` -> full copy

---

## 4) `min()`, `max()`, and `sorted()` on String

```python
print(min(S1))
print(max(S1))
sorted_S1 = sorted(S1)
print(sorted_S1)
```

- `min(S1)` returns smallest character by Unicode/ASCII order.
- `max(S1)` returns largest character by Unicode/ASCII order.
- `sorted(S1)` returns a **list** of sorted characters, not a string.

If you want sorted output as string:

```python
"".join(sorted(S1))
```

---

## 5) Concatenation and Repetition

```python
S1 = "sir"
S2 = "mysir"
S3 = S1 + S2
S4 = S1 * 3
```

- `+` joins strings (concatenation).
- `*` repeats string multiple times.

Results:

- `S3` -> `sirmysir`
- `S4` -> `sirsirsir`

---

## 6) String Comparison Operators

```python
S1 = "abc"
S2 = "xyz"
print(S1 == S2)
print(S1 != S2)
print(S1 > S2)
print(S1 < S2)
```

Comparison happens **lexicographically** (dictionary order), character by character.

- `==` checks equality
- `!=` checks not equal
- `>` checks greater than
- `<` checks less than

Because `'a'` comes before `'x'`, `"abc" < "xyz"` is `True`.

Note:

- Uppercase and lowercase have different Unicode values.
- Example: `"A" < "a"` is `True`.

---

## 7) Important String Methods

You listed these methods in code comments. Here is what each does:

### 7.1 `index(substring)`

- Returns first index of substring.
- Raises `ValueError` if not found.

```python
s = "hello"
s.index("e")   # 1
# s.index("z") -> ValueError
```

### 7.2 `find(substring)`

- Returns first index of substring.
- Returns `-1` if not found (no error).

```python
s.find("e")    # 1
s.find("z")    # -1
```

### 7.3 `count(substring)`

- Counts how many times substring appears.

```python
"banana".count("a")  # 3
```

### 7.4 `replace(old, new)`

- Replaces all occurrences of `old` with `new`.

```python
"apple".replace("p", "P")  # aPPle
```

### 7.5 `upper()`

- Converts all letters to uppercase.

```python
"hello".upper()  # HELLO
```

### 7.6 `lower()`

- Converts all letters to lowercase.

```python
"HELLO".lower()  # hello
```

### 7.7 `strip()`

- Removes spaces/newline/tab from both ends.

```python
"  hi  ".strip()  # hi
```

### 7.8 `split(delimiter)`

- Breaks a string into list of parts.
- Default delimiter is whitespace.

```python
"a b c".split()      # ['a', 'b', 'c']
"a-b-c".split("-")  # ['a', 'b', 'c']
```

### 7.9 `join(iterable)`

- Joins list/tuple of strings into one string.
- Called on delimiter string.

```python
"-".join(["a", "b", "c"])  # a-b-c
" ".join(["a", "b", "c"])  # a b c
```

---

## 8) Using Methods in Your Example

```python
s1 = "mysirg education system"
```

- `s1.index("s")` -> first `s` index
- `s1.find("s")` -> same result when found
- `s1.count("s")` -> total `s`
- `s1.replace("s", "S")` -> every `s` becomes `S`
- `s1.upper()` -> all uppercase
- `s1.lower()` -> all lowercase
- `s1.strip()` -> trims outer spaces (no visible change if no outer spaces)
- `s1.split()` -> list of words
- `"-".join(s1.split())` -> words joined by hyphen

---

## 9) Formatted String Literals (f-strings)

```python
a, b = 10, 20
print(f"The sum of {a} and {b} is {a+b}.")
```

An f-string starts with `f` before quotes.

- Put variable/expression inside `{}`.
- Python evaluates and inserts result in the string.

Another example:

```python
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")
```

Why f-strings are preferred:

- Easy to read
- Fast and modern
- Supports expressions directly

---

## 10) Split and Join (Practical Pattern)

```python
sentence = "Hello, how are you?"
words = sentence.split()
delimiter = "-"
joined_sentence = delimiter.join(words)
```

- `split()` converts sentence into list of words.
- `join()` rebuilds sentence with a custom separator.

Output idea:

- words -> `['Hello,', 'how', 'are', 'you?']`
- joined -> `Hello,-how-are-you?`

You also used space delimiter:

```python
delimiter = " "
joined_sentence = delimiter.join(words)
```

This gives the sentence back with normal spaces.

---

## 11) Program: Count Occurrences of Each Character

Your code:

```python
user_input = input("Enter a string: ")
char_count = {}
for char in user_input:
	char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
	print(f"Character '{char}' occurs {count} times.")
```

### Step-by-step explanation

1. Take input string from user.
2. Create empty dictionary `char_count`.
3. Loop through each character.
4. `char_count.get(char, 0)` means:
   - if `char` exists, get old count
   - else use `0`
5. Add `1` to count and store back.
6. Print each character and final count.

Example input: `hello`

- `h` -> 1
- `e` -> 1
- `l` -> 2
- `o` -> 1

---

## 12) Common Mistakes to Avoid

- Writing `S1[100]` when index does not exist.
- Confusing `index()` and `find()` when value may be missing.
- Expecting `sorted(string)` to return string (it returns list).
- Using `join()` incorrectly:

Wrong:

```python
words.join("-")
```

Correct:

```python
"-".join(words)
```

---

## 13) Quick Revision

- String = immutable sequence of characters.
- Indexing = access one character.
- Slicing = access part of string.
- `+` and `*` = concatenate and repeat.
- Comparisons are lexicographical.
- Key methods: `index`, `find`, `count`, `replace`, `upper`, `lower`, `strip`, `split`, `join`.
- f-strings = readable formatting.
- Dictionary + loop is great for frequency counting.

These are the exact topics covered in your `main.py`, now explained from scratch.
