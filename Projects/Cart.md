# Digital Shopping Cart - Complete Line-by-Line Explanation

Ye program ek simple command-line shopping cart system hai jisme user menu ke through items add, remove, view aur exit kar sakta hai.

---

## LINE-BY-LINE CODE BREAKDOWN

### Line 1: Initialize Empty Cart

**Code:**
```python
cart = []
```

**Explanation:**
- `cart` ek variable hai jo ek list create karta hai.
- Square brackets `[]` iska matlab empty list.
- Iska use: Cart mein items store karne ke liye.
- Data type: `list`
- Initial value: empty (koi items nahi)

---

### Line 3: Welcome Message

**Code:**
```python
print("Welcome to Digital Shopping Cart")
```

**Explanation:**
- `print()` function output screen par display karta hai.
- String `"Welcome to Digital Shopping Cart"` welcome message hai.
- Ye program start hone par ek hi baar print hota hai.
- Output: `Welcome to Digital Shopping Cart`

---

### Line 5: Infinite Loop Start

**Code:**
```python
while True:
```

**Explanation:**
- `while` ek loop statement hai.
- `True` condition hamesha true hi rehti hai.
- Matlab ye loop infinite chalta rahega.
- Exit sirf `break` se hota hai.
- Colon `:` se indentation rule apply hota hai.

---

### Line 6-10: Menu Display

**Code:**
```python
    print("\nChoose an option:")
    print("Press 1: Add item to cart")
    print("Press 2: Remove item from cart")
    print("Press 3: View cart and total item count")
    print("Press 4: Exit")
```

**Explanation:**
- `\n` ka matlab newline (ek line break).
- Pehla `print()`: heading dikhata hai.
- Agla 4 `print()` statements: menu options display karte hain.
- Loop ke har iteration mein ye menu repeat hota hai.
- Output:
  ```
  Choose an option:
  Press 1: Add item to cart
  Press 2: Remove item from cart
  Press 3: View cart and total item count
  Press 4: Exit
  ```

---

### Line 12: User Input Lena

**Code:**
```python
    choice = input("Enter your choice (1/2/3/4): ")
```

**Explanation:**
- `input()` user se keyboard se input leta hai.
- String parameter `"Enter your choice (1/2/3/4): "` prompt dikhata hai.
- Input ke baad `Enter` key press karna padta hai.
- Return value hamesha string hoti hai (bhale number type karo).
- `choice` variable mein ye string store hota hai.
- Example: agar user `1` type kare, to `choice = "1"` (string form mein)

---

### Line 14-20: Option 1 - Add Item Logic

**Code:**
```python
    if choice == "1":
        item_name = input("Enter item name to add: ").strip()
        if item_name:
            cart.append(item_name)
            print(f"'{item_name}' has been added to your cart.")
        else:
            print("Item name cannot be empty.")
```

**Breakdown:**

**Line 14:**
```python
if choice == "1":
```
- `if` conditional statement.
- `choice == "1"` check karta hai: kya user ne "1" enter kiya?
- `==` equality operator (comparison).
- Colon `:` se next block indented hona chahiye.

**Line 15:**
```python
item_name = input("Enter item name to add: ").strip()
```
- `input()` user se item name leta hai.
- `.strip()` method: extra spaces (start aur end mein) remove karta hai.
- Example: `"  apple  ".strip()` becomes `"apple"`
- Result `item_name` variable mein store hota hai.

**Line 16:**
```python
if item_name:
```
- Nested `if` statement.
- `if item_name:` check karta hai: kya item_name empty string nahi hai?
- Empty string: `""` (false)
- Non-empty string: koi bhi value (true)

**Line 17:**
```python
cart.append(item_name)
```
- `append()` method list mein item add karta hai.
- Last position mein add hota hai.
- Example: `["milk"].append("bread")` becomes `["milk", "bread"]`

**Line 18:**
```python
print(f"'{item_name}' has been added to your cart.")
```
- `f"..."` = f-string (formatted string).
- `{item_name}` placeholder ko actual value se replace karta hai.
- Example: agar item_name = "apple", to output: `'apple' has been added to your cart.`

**Line 19:**
```python
else:
    print("Item name cannot be empty.")
```
- `else`: agar item_name empty ho (jab user sirf spaces type kare ya kuch na type kare).
- Warning message print hota hai.

---

### Line 22-27: Option 2 - Remove Item Logic

**Code:**
```python
    elif choice == "2":
        item_name = input("Enter item name to remove: ").strip()
        if item_name in cart:
            cart.remove(item_name)
            print(f"'{item_name}' has been removed from your cart.")
        else:
            print(f"'{item_name}' is not in your cart.")
```

**Breakdown:**

**Line 22:**
```python
elif choice == "2":
```
- `elif` = "else if" (agar pehla condition false ho, to ye check karo).
- Ye tab execute hota hai jab user ne "2" enter kiya ho.

**Line 23:**
```python
item_name = input("Enter item name to remove: ").strip()
```
- User se remove karne ke liye item name liya jata hai.
- Same as Line 15.

**Line 24:**
```python
if item_name in cart:
```
- `in` operator membership check karta hai.
- Check: kya item_name list `cart` mein exist karta hai?
- True/False return karta hai.

**Line 25:**
```python
cart.remove(item_name)
```
- `remove()` method item ko list se delete karta hai.
- First occurrence remove hota hai.
- Agar item nahi hota to error deta tha (isliye pehle check karate hain).

**Line 26:**
```python
print(f"'{item_name}' has been removed from your cart.")
```
- Success message print hota hai.

**Line 27:**
```python
else:
    print(f"'{item_name}' is not in your cart.")
```
- Agar item list mein nahi tha to ye message dikhta hai.

---

### Line 29-37: Option 3 - View Cart Logic

**Code:**
```python
    elif choice == "3":
        if cart:
            print("\nYour cart items are:")
            for index, item in enumerate(cart, start=1):
                print(f"{index}. {item}")
        else:
            print("\nYour cart is empty.")

        print(f"Total items in cart: {len(cart)}")
```

**Breakdown:**

**Line 29:**
```python
elif choice == "3":
```
- User ne option 3 select kiya.

**Line 30:**
```python
if cart:
```
- Check: kya cart empty nahi hai?
- Empty list `[]` = False
- Non-empty list = True

**Line 31:**
```python
print("\nYour cart items are:")
```
- Heading print hota hai.
- `\n` se line break hota hai.

**Line 32-33:**
```python
for index, item in enumerate(cart, start=1):
    print(f"{index}. {item}")
```

- `for` loop: list ke har element par iterate karta hai.
- `enumerate(cart, start=1)`: 
  - Pairs banata hai: (position, value)
  - `start=1` se numbering 0 se nahi, 1 se shuru hoti hai.
  - Example: `enumerate(["milk", "bread"], start=1)` gives `(1, "milk")`, `(2, "bread")`
- `index` = position number
- `item` = actual item name
- Print format: `1. milk`, `2. bread`

**Line 35:**
```python
else:
    print("\nYour cart is empty.")
```
- Agar cart khali ho tab ye message.

**Line 37:**
```python
print(f"Total items in cart: {len(cart)}")
```
- `len(cart)` list mein total items ki count return karta hai.
- Ye line `if/else` ke bahar hai, to dono cases mein print hota hai.
- Output: `Total items in cart: 0` (agar empty) ya `Total items in cart: 2` (agar 2 items)

---

### Line 39-42: Option 4 - Exit Logic

**Code:**
```python
    elif choice == "4":
        print("Thank you for using Digital Shopping Cart. Goodbye!")
        break
```

**Breakdown:**

**Line 39:**
```python
elif choice == "4":
```
- User ne option 4 select kiya.

**Line 40:**
```python
print("Thank you for using Digital Shopping Cart. Goodbye!")
```
- Goodbye message.

**Line 41:**
```python
break
```
- `break` statement loop ko immediately terminate karta hai.
- `while True` loop se exit hota hai.
- Program khatam ho jata hai.

---

### Line 43-44: Invalid Input Handling

**Code:**
```python
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
```

**Breakdown:**

**Line 43:**
```python
else:
```
- Agar user ne 1, 2, 3, 4 ke alawa kuch aur type kiya (jaise `5`, `abc`, blank).

**Line 44:**
```python
print("Invalid choice. Please enter 1, 2, 3, or 4.")
```
- Friendly error message.
- Loop continue rehta hai.
- User ko phir se menu dikhta hai.

---

## SUMMARY TABLE

| Line(s) | Purpose | Key Concept |
|---------|---------|------------|
| 1 | Initialize empty cart | List creation |
| 3 | Welcome message | Output |
| 5 | Start infinite loop | `while True` |
| 6-10 | Display menu options | Menu interface |
| 12 | Get user choice | Input |
| 14-20 | Add item logic | `append()`, `.strip()` |
| 22-27 | Remove item logic | `remove()`, `in` operator |
| 29-37 | View cart logic | `enumerate()`, `len()` |
| 39-42 | Exit program | `break` |
| 43-44 | Handle invalid input | `else` clause |

---

## 1. Program Goal

Program ka objective hai:

1. Cart ko list ke form mein maintain karna.
2. User ko repeated menu options dena.
3. User choice ke hisaab se action perform karna.
4. Program ko tab tak chalana jab tak user exit na kare.

## 2. Core Data Structure

`cart = []`

- `cart` ek list hai.
- Start mein empty hai.
- Ismein shopping items string form mein store hote hain.

Example:

- Empty cart: `[]`
- Add ke baad: `["milk", "bread"]`

## 3. Program Start

`print("Welcome to Digital Shopping Cart")`

- Ye user ko welcome message show karta hai.
- Iske baad program menu loop mein chala jata hai.

## 4. Infinite Loop

`while True:`

- Iska matlab loop continuously chalta rahega.
- Exit sirf `break` se hoga jab user option `4` choose karega.

## 5. Menu Display

Har iteration mein ye options print hote hain:

1. Add item
2. Remove item
3. View cart + count
4. Exit

Input line:

`choice = input("Enter your choice (1/2/3/4): ")`

- `input()` हमेशा string return karta hai.
- Isliye comparisons bhi string se ho rahi hain (`"1"`, `"2"`, etc.).

## 6. Option-Wise Logic

### Option 1: Add Item

Condition:

`if choice == "1":`

Steps:

1. User se item ka naam liya jata hai.
2. `.strip()` use karke extra spaces remove ki jati hain.
3. Agar item empty nahi hai to `cart.append(item_name)` se add kar dete hain.
4. Agar user blank input de to warning message milta hai.

Why `.strip()`?

- User agar sirf spaces type kare (`"   "`), to wo valid item na bane.

### Option 2: Remove Item

Condition:

`elif choice == "2":`

Steps:

1. User se remove karne ke liye item name liya jata hai.
2. Check hota hai: `if item_name in cart:`
3. Agar item present hai to `cart.remove(item_name)` se delete hota hai.
4. Agar item present nahi hai to error ki jagah friendly message print hota hai.

Important safety point:

- Direct `cart.remove(item_name)` without check karne par error aa sakta hai (`ValueError`) agar item list mein nahi ho.

### Option 3: View Cart + Total Count

Condition:

`elif choice == "3":`

Steps:

1. Check hota hai cart empty hai ya nahi.
2. Agar cart mein items hain to:
   - heading print hoti hai
   - `enumerate(cart, start=1)` se numbered list print hoti hai
3. Agar cart empty hai to `Your cart is empty.` print hota hai.
4. Har case mein total count print hota hai:

`len(cart)`

Example output:

- `1. Milk`
- `2. Bread`
- `Total items in cart: 2`

### Option 4: Exit

Condition:

`elif choice == "4":`

Steps:

1. Goodbye message print hota hai.
2. `break` execute hota hai.
3. `while True` loop terminate ho jata hai.

### Invalid Input Handling

Condition:

`else:`

- Agar user `1/2/3/4` ke alawa kuch bhi enter karta hai (jaise `7`, `abc`, blank), to program crash nahi karta.
- Friendly guidance message deta hai.

## 7. Concepts Covered in This Program

Is single program mein aapne multiple concepts combine kiye hain:

1. Variables: `cart`, `choice`, `item_name`
2. List operations: `append()`, `remove()`, membership (`in`), `len()`
3. Conditional logic: `if / elif / else`
4. Looping: `while True`
5. Loop control: `break`
6. Input handling: `input()` + `.strip()`
7. Formatted strings: `f"..."`
8. Enumeration: `enumerate(..., start=1)`

## 8. Dry Run (Step-by-Step Example)

Initial state:

- `cart = []`

User actions:

1. Input `1` -> add `apple` -> cart becomes `["apple"]`
2. Input `1` -> add `milk` -> cart becomes `["apple", "milk"]`
3. Input `3` -> shows both items and count `2`
4. Input `2` -> remove `apple` -> cart becomes `["milk"]`
5. Input `3` -> shows only `milk` and count `1`
6. Input `4` -> program exits

## 9. Time Complexity (Simple View)

1. Add item (`append`) -> average `O(1)`
2. Remove item by value (`remove`) -> `O(n)` because search needed
3. Membership check (`in`) -> `O(n)`
4. View complete cart -> `O(n)`

Yahan `n` = cart mein items ki sankhya.

## 10. Possible Improvements

1. Duplicate items allow/deny control (same item multiple times add karna hai ya nahi).
2. Quantity support add karo (`apple x 2`).
3. Price add karke total bill calculate karo.
4. Case-insensitive remove (e.g., `Milk` and `milk` same treat ho).
5. Save/load cart using file handling (`.txt`/`.json`).
6. Input normalization (spaces cleanup and title/lower formatting).

## 11. Short Summary

Ye program beginner level ke liye excellent practice hai kyunki isme real-world problem ke through list management, loops, conditions aur input handling ek saath apply hote hain. Agar aap isko quantity + pricing tak extend karte ho, to ye mini e-commerce cart project ban jayega.
