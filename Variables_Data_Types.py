# Day 01 – Python Variables and Data Types

## Learning Objectives

Today I learned:

- How to create and assign variables in Python.
- How to identify Python data types.
- How to display values using `print()`.
- How to check data types using `type()`.
- How to reassign values to variables.
- How to perform basic mathematical calculations.
- How to use Boolean values.

---

## Challenge 01 – Student Information

**Task:** Create variables to store student information, display the values and identify their data types.

### Corrected Solution

```python
name = "Harini"
age = 21
degree = "AI"
university = "SLIIT"
current_gpa = 3.25
studying = True

# Display student information
print(name)
print(age)
print(degree)
print(university)
print(current_gpa)
print(studying)

# Display data types
print(type(name))
print(type(age))
print(type(degree))
print(type(university))
print(type(current_gpa))
print(type(studying))
```

### Expected Data Types

| Variable | Value | Data Type |
|---|---|---|
| name | Harini | str |
| age | 21 | int |
| degree | AI | str |
| university | SLIIT | str |
| current_gpa | 3.25 | float |
| studying | True | bool |

### Corrections I Learned

**1. String vs Float**

Incorrect:
```python
current_gpa = "3.25"
```

Correct:
```python
current_gpa = 3.25
```

Quotation marks make the value a string. Without quotation marks, a decimal number is a float.

**2. Boolean Values**

Incorrect:
```python
studying = true
```

Correct:
```python
studying = True
```

Python is case-sensitive. Boolean keywords must start with capital letters: `True` and `False`.

**3. Python Comments**

Incorrect:
```python
// This is a comment
```

Correct:
```python
# This is a comment
```

Python uses `#` for comments.

---

## Challenge 02 – Variable Reassignment

**Task:** Understand how variables behave when their values change.

### Corrected Solution

```python
x = 10
y = 20

# Assign the calculation result to z
z = x + y

# Task 1: Display z
print("Initial value of z:", z)

# Task 2: Change x
x = 50

# Task 3: Display z again
print("Value of z after changing x:", z)

# Task 4: Recalculate z
z = x + y

print("Updated value of z:", z)

# Task 5: Change x into a string
x = "Python"

# Task 6: Display x and its data type
print("Updated x:", x)
print("Data type:", type(x))
```

### Expected Output

```text
Initial value of z: 30
Value of z after changing x: 30
Updated value of z: 70
Updated x: Python
Data type: <class 'str'>
```

### What I Learned

Initially:

```python
x = 10
y = 20
z = x + y
```

Python calculates:

10 + 20 = 30

Therefore, `z` stores 30.

When I change `x`:

```python
x = 50
```

The value of `z` remains 30.

Why?

Python does not automatically recalculate an earlier assignment. It evaluates the expression when the assignment statement executes.

To update `z`, I must write:

```python
z = x + y
```

Again.

**Important concept:** Assigning a calculation result to a variable does not create a permanent connection between the variables.

---

## Challenge 03 – Data Type Detective

**Task:** Identify the data type of each variable and verify it using `type()`.

### Corrected Solution

```python
a = 100
b = 25.5
c = "100"
d = True
e = 10 + 5
f = "Hello" + " Python"
g = 10.0

# Display values and data types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
```

### Correct Answers

| Variable | Value | Data Type |
|---|---|---|
| a | 100 | int |
| b | 25.5 | float |
| c | "100" | str |
| d | True | bool |
| e | 15 | int |
| f | Hello Python | str |
| g | 10.0 | float |

### Corrections I Learned

**1. Why is `e` an integer and not an error?**

```python
e = 10 + 5
```

Python calculates the expression and stores the result:

10 + 5 = 15

The result is an integer.

**2. Why is `f` a string?**

```python
f = "Hello" + " Python"
```

The `+` operator joins two strings. This is called string concatenation.

**3. Why is `g` a float and not a double?**

```python
g = 10.0
```

Python uses the `float` data type for decimal numbers. It does not have a separate built-in `double` type like Java.

---

## Challenge 04 – Shopping Calculator

**Task:** Calculate the total shopping price and final price after applying a discount.

### Corrected Solution

```python
# Store item prices
laptop = 150000
mouse = 2500
keyboard = 4500

# Calculate total price
total = laptop + mouse + keyboard

# Store discount amount
discount_amount = 10000

# Calculate final price
final_price = total - discount_amount

# Display results
print("Laptop Price:", laptop)
print("Mouse Price:", mouse)
print("Keyboard Price:", keyboard)

print("Total Price:", total)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
```

### Expected Output

```text
Laptop Price: 150000
Mouse Price: 2500
Keyboard Price: 4500
Total Price: 157000
Discount Amount: 10000
Final Price: 147000
```

### Corrections I Learned

My original attempt:

```python
dis_amount = total - amount
```

The problem was that `amount` had not been assigned a value.

The correct approach is:

```python
discount_amount = 10000
final_price = total - discount_amount
```

**Important concept:** Before using a variable in a calculation, make sure it has already been assigned a value.

---

## Challenge 05 – Mini Challenge: Personal Profile

**Task:** Create a personal profile using variables, Boolean values, formatted output, data types and variable reassignment.

### Corrected Solution

```python
# Store personal information
name = "Harini"
age = 21
university = "SLIIT"
degree = "AI"
current_gpa = 3.25

# Store AI interest
interested = True

# Display personal profile
print("===== STUDENT PROFILE =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"University: {university}")
print(f"Degree: {degree}")
print(f"Current CGPA: {current_gpa}")
print(f"Interested in AI: {interested}")

# Display data types
print("\n===== DATA TYPES =====")
print(type(name))
print(type(age))
print(type(university))
print(type(degree))
print(type(current_gpa))
print(type(interested))

# Update CGPA
current_gpa = 3.256

# Display updated profile
print("\n===== UPDATED STUDENT PROFILE =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"University: {university}")
print(f"Degree: {degree}")
print(f"Updated CGPA: {current_gpa}")
print(f"Interested in AI: {interested}")
```

### What I Learned

**1. Formatted Strings (f-strings)**

Instead of printing every value separately, I can use an f-string:

```python
print(f"Name: {name}")
```

The `f` allows Python to insert the variable's value inside the string using `{}`.

**2. Variable Reassignment**

Initially:

```python
current_gpa = 3.25
```

Later:

```python
current_gpa = 3.256
```

Python allows me to assign a new value to an existing variable.

---

## Important Concepts Learned – Day 01

| Concept | Explanation |
|---|---|
| Variable | A name used to refer to a value |
| Assignment (`=`) | Assigns a value to a variable |
| `print()` | Displays output |
| `type()` | Checks the type of an object |
| `int` | Whole numbers |
| `float` | Decimal numbers |
| `str` | Text |
| `bool` | True or False |
| Reassignment | Assigning a new value to an existing variable |
| String concatenation | Joining strings using `+` |
| f-string | Inserts variable values into formatted strings |

### Python vs Java – My Observation

In Java, I need to declare a variable's type:

```java
int age = 21;
double cgpa = 3.25;
String name = "Harini";
```

In Python, I can assign values directly:

```python
age = 21
cgpa = 3.25
name = "Harini"
```

Python determines the type of the assigned object automatically. This is called **dynamic typing**.

---

## Day 01 – Submission Checklist

- [x] Challenge 01 – Student Information
- [x] Challenge 02 – Variable Reassignment
- [x] Challenge 03 – Data Type Detective
- [x] Challenge 04 – Shopping Calculator
- [x] Challenge 05 – Personal Profile
- [x] Reviewed mistakes and corrected code
- [x] Practised variables and data types

## Final Reflection

Today I learned the fundamentals of Python variables and data types.

At first, I was confused about Boolean values, assigning mathematical expressions and how variable reassignment works. Through the challenges, I understood that Python executes assignment statements in order and does not automatically recalculate previously stored results.

I also learned that Python uses `int`, `float`, `str` and `bool` data types, and that I can check them using `type()`.

**Day 01 completed – Building my Python foundation, one concept at a time!**
