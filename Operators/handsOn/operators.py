"""
Python Operators - Assignment Notes

This file contains:
1. Definitions of Python operators
2. Examples with outputs
3. Practice questions for each type of operator

Topic: Python Operators
"""


# ============================================================

# Operators are special symbols in Python which are used to perform operations
# on variables and values.

# Example:
a = 10
b = 5

print( a + b)

# Output:
#  15

# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

# Arithmetic operators are used to perform mathematical calculations.

# Operators:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# %   Modulus
# **  Power

x = 20
y = 6

print("\nArithmetic Operators:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Power:", x ** 2)

# Output:
# Addition: 26
# Subtraction: 14
# Multiplication: 120
# Division: 3.3333333333333335
# Floor Division: 3
# Modulus: 2
# Power: 400



# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

# Comparison operators are used to compare two values.
# They always return True or False.

# Operators:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

m = 50
n = 30

print("\nComparison Operators:")
print("m == n:", m == n)
print("m != n:", m != n)
print("m > n:", m > n)
print("m < n:", m < n)
print("m >= n:", m >= n)
print("m <= n:", m <= n)

# Output:
# m == n: False
# m != n: True
# m > n: True
# m < n: False
# m >= n: True
# m <= n: False



# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================

# Logical operators are used to combine multiple conditions.

# Operators:
# and  Returns True if both conditions are True
# or   Returns True if at least one condition is True
# not  Reverses the result

age = 21
has_id = True

print("\nLogical Operators:")

if age >= 18 and has_id:
    print("Allowed to enter")
else:
    print("Not allowed")

# Output:
# Allowed to enter

attendance = 60
medical_certificate = True

if attendance >= 75 or medical_certificate:
    print("Allowed for exam")
else:
    print("Not allowed for exam")

# Output:
# Allowed for exam

is_raining = False

if not is_raining:
    print("Can go outside")

# Output:
# Can go outside

# ============================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================

# Assignment operators are used to assign and update values.

# Operators:
# =    Assign
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# %=   Modulus and assign
# //=  Floor divide and assign
# **=  Power and assign

balance = 5000

print("\nAssignment Operators:")

balance += 2000
print("After deposit:", balance)

balance -= 1000
print("After withdrawal:", balance)

balance *= 2
print("After doubling:", balance)

balance /= 2
print("After half:", balance)

# Output:
# After deposit: 7000
# After withdrawal: 6000
# After doubling: 12000
# After half: 6000.0

# USE CASES:

# Strings
# name = "Unnati"
# name += " Tripathi"

# # Unnati Tripathi
# Lists    : extend the same list
# nums = [1, 2]
# nums += [3, 4]

# # [1, 2, 3, 4]

# ============================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================

# Membership operators are used to check whether a value exists
# inside a sequence like list, tuple, string, set, or dictionary.

# Operators:
# in
# not in

subjects = ["Python", "DBMS", "Java", "C++"]

print("\nMembership Operators:")

print("Python" in subjects)
print("React" not in subjects)

# Output:
# True
# True

name = "Unnati"

print("n" in name)

# Output:
# True


# Note:
# In dictionary, membership checks keys by default.

student = {
    "name": "Unnati",
    "age": 21
}

print("name" in student)
print("Unnati" in student)

# Output:
# True
# False


# ============================================================
# 6. IDENTITY OPERATORS
# ============================================================

# Identity operators are used to check whether two variables refer
# to the same object in memory.

# Operators:
# is
# is not

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("\nIdentity Operators:")

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

# Output:
# True
# False
# True



# ============================================================
# 7. BITWISE OPERATORS
# ============================================================

# Bitwise operators work on binary numbers.
# They are mostly used in low level programming and competitive programming.

# Operators:
# &   Bitwise AND
# |   Bitwise OR
# ^   Bitwise XOR
# ~   Bitwise NOT
# <<  Left Shift
# >>  Right Shift

p = 5
q = 3

print("\nBitwise Operators:")

print("p & q:", p & q)
print("p | q:", p | q)
print("p ^ q:", p ^ q)
print("p << 1:", p << 1)
print("p >> 1:", p >> 1)

# Output:
# p & q: 1
# p | q: 7
# p ^ q: 6
# p << 1: 10
# p >> 1: 2


# ============================================================
# 8. OPERATOR PRECEDENCE
# ============================================================

# Operator precedence decides which operator runs first.

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4

print("\nOperator Precedence:")
print(result1)
print(result2)

# Output:
# 14
# 20


# Explanation:
# In result1, multiplication happens first.
# In result2, parentheses happen first.


# Common precedence order:
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. Comparison operators
# 6. not
# 7. and
# 8. or

