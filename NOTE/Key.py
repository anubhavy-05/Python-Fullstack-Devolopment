# QUESTION 1

x=int(7.9) # Typecasting a float to an integer, which will truncate the decimal part and give 7.truncation means that the decimal part is removed and only the whole number part is kept.
print(x) # Output: 7

# QUESTION 2

y=float(7) # Typecasting an integer to a float, which will give 7.0.
print(y) # Output: 7.0

# round() is a built-in function in Python that rounds a number to a specified number of decimal places. If the number of decimal places is not specified, it rounds to the nearest integer.rules of rounding: If the decimal part is less than 0.5, the number is rounded down. If the decimal part is 0.5 or greater, the number is rounded up.

# QUESTION 3

z=round(7.8) # Rounds to the nearest integer.
print(z) # Output: 8
z=round(7.8, 1) # Rounds to 1 decimal place.
print(z) # Output: 7.8
