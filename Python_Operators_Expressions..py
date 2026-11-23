# Day 03 – Python Arithmetic Operators 🐍

**365 Days of Python Challenge**

## Challenge 01 – Basic Calculator 🧮

```python
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```

**Output:**
```text
Addition: 26
Subtraction: 14
Multiplication: 120
Division: 3.3333333333333335
Floor Division: 3
Modulus: 2
Exponentiation: 64000000
```

## Challenge 02 – Even or Odd Detector 🔢

```python
number = 17

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

**Output:**
```text
Odd Number
```

**Concept:** The modulus operator (`%`) returns the remainder. If the remainder is 0 when divided by 2, the number is even.

## Challenge 03 – Shopping Calculator 🛒

```python
laptop = 150000
mouse = 2500
keyboard = 4500

total = laptop + mouse + keyboard

discount = total * 0.10

final_price = total - discount

print("Laptop Price:", laptop)
print("Mouse Price:", mouse)
print("Keyboard Price:", keyboard)
print("Total Price:", total)
print("Discount (10%):", discount)
print("Final Price:", final_price)
```

**Output:**
```text
Laptop Price: 150000
Mouse Price: 2500
Keyboard Price: 4500
Total Price: 157000
Discount (10%): 15700.0
Final Price: 141300.0
```

## Challenge 04 – Area Calculator 📐

### A. Rectangle

```python
length = 15
width = 8

rectangle_area = length * width

print("Rectangle Area:", rectangle_area)
```

**Output:**
```text
Rectangle Area: 120
```

### B. Square

```python
side = 12

square_area = side ** 2

print("Square Area:", square_area)
```

**Output:**
```text
Square Area: 144
```

**Concept:** The exponentiation operator (`**`) calculates powers. For example, `12 ** 2` means 12 × 12.

## Challenge 05 – Number Power Challenge 🚀

```python
number = 5

square = number ** 2
cube = number ** 3
division = number / 2
floor_division = number // 2
remainder = number % 2

print("Square:", square)
print("Cube:", cube)
print("Division:", division)
print("Floor Division:", floor_division)
print("Remainder:", remainder)
```

**Output:**
```text
Square: 25
Cube: 125
Division: 2.5
Floor Division: 2
Remainder: 1
```

## Bonus Challenge – Mini Calculator ⭐

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division is not possible because the second number is zero.")
```

**Example Output:**
```text
Enter the first number: 20
Enter the second number: 5

Addition: 25.0
Subtraction: 15.0
Multiplication: 100.0
Division: 4.0
```

## What I Learned Today 📚

- How to use Python arithmetic operators.
- The difference between normal division (`/`) and floor division (`//`).
- How to calculate remainders using modulus (`%`).
- How to calculate powers using exponentiation (`**`).
- How to use arithmetic operators in real-world calculations.
- How to use `if-else` to identify even and odd numbers.
- How to collect user input using `input()` and convert it using `float()`.

## Day 03 Completion Checklist

- [x] Challenge 01 – Basic Calculator
- [x] Challenge 02 – Even or Odd Detector
- [x] Challenge 03 – Shopping Calculator
- [x] Challenge 04 – Area Calculator
- [x] Challenge 05 – Number Power Challenge
- [x] Bonus – Mini Calculator

**Day 03 completed! One more day of learning, experimenting, and improving my Python skills. 🚀**

#365DaysOfPython #Python #LearningPython #PythonProgramming
