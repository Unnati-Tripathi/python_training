
# ======================================================
# BUILT-IN PYTHON FUNCTIONS, TRY/EXCEPT, FINALLY
# PRACTICE FILE
# ======================================================

# Because enumerate gives both:

# index
# value

print("="*50)
print("BUILT-IN FUNCTIONS")
print("="*50)

nums = [10, 20, 30, 40, 50]

# arr = [12 , 34 , 50]


# print(len(arr));
# print(max(arr));
import math
print("len:", len(nums))
print("max:", max(nums))
print("min:", min(nums))
print("sum:", sum(nums))
print("sorted:", sorted([5,2,8,1]) )
print("ceil" , math.ceil(3.2));
print("floor" , math.floor(3.2))

print("abs:", abs(-15))
print("round:", round(3.14159, 2))

# 3%5 = 3
# lambda  functions , sorting based upon the basis of remainder


# Returns index and value together.
print("\nEnumerate Example")
names = ["Amit", "Sara", "Unnati"]

for idx, name in enumerate(names, start=1):
    print(idx, name)




# # Problem Without enumerate()
# # If you want index + value:

# names = ["Amit", "Sara", "Unnati"]
# for i in range(len(names)):
#     print(i, names[i])




# What does enumerate return?
names = ["Amit", "Sara", "Unnati"]
x = enumerate(names)
print(x)
# It returns an enumerate object (iterator).

print(list(enumerate(names)))
# Output:
# [(0, 'Amit'),
#  (1, 'Sara'),
#  (2, 'Unnati')]



# with stringss
word = "Python"
for index, ch in enumerate(word):
    print(index, ch)



print("\nZip Example")
# zip() is used to combine multiple iterables (lists, tuples, strings, etc.) element by element.
# zip() stops when the shortest iterable ends.

marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)


cities = ["Delhi", "Lucknow", "Kanpur"]

for n, m, c in zip(names, marks, cities):
    print(n, m, c)



print("\nAny and All")
print(any([0,0,1]))
print(all([1,2,3]))
print(all([1,0,3]))




# ======================================================
# TRY EXCEPT
# ======================================================

print("\n" + "="*50)
print("TRY EXCEPT")
print("="*50)

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    nums = [10,20,30]
    print(nums[10])

except IndexError:
    print("Index out of range")

try:
    value = int("abc")

except ValueError:
    print("Invalid integer conversion")




# Multiple Exceptions
try:
    num = int(input())
    print(100 / num)

except ValueError:
    print("Enter valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")




# exception by e 
try:
    print(10 / 0)

except Exception as e:
    print(e) 




# ======================================================
# FINALLY
# ======================================================
# Runs whether error occurs or not.

print("\n" + "="*50)
print("FINALLY")
print("="*50)

try:
    print("Inside Try")

finally:
    print("Inside Finally")



try:
    result = 10 / 0

except ZeroDivisionError:
    print("Division Error")

finally:
    print("Cleanup Code Executed")





# with else 
try:
    print(10 / 2)

except:
    print("Error")

else:
    print("Success")

finally:
    print("Done")







# FLOW:-

# try
#  │
#  ├── Exception?
#  │      │
#  │      ├── Yes → except
#  │      │
#  │      └── No  → else
#  │
#  └─────────────→ finally


# Common Exceptions
# Exception	Example
# ZeroDivisionError	10/0
# ValueError	int("abc")
# IndexError	lst[10]
# KeyError	d["name"] missing
# TypeError	"1" + 2
# FileNotFoundError	Open missing file