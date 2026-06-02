"""
Assignment : Python Set

"""


# -------------------------------
# Introduction to Set
# -------------------------------

# A set is a collection of unique values.

s = {1, 2, 3, 4}

print("Original Set :", s)

# Output:
# Original Set : {1, 2, 3, 4}


# -------------------------------
# Duplicate values are removed
# -------------------------------

a = {1, 2, 2, 3, 3, 4}

print("Set after removing duplicates :", a)

# Output:
# Set after removing duplicates : {1, 2, 3, 4}


# -------------------------------
# Creating Sets
# -------------------------------

s1 = {10, 20, 30}

s2 = set([1, 2, 2, 3, 4])

s3 = set("hello")

print(s1)
print(s2)
print(s3)

# Output:
# {10, 20, 30}
# {1, 2, 3, 4}
# {'h', 'e', 'l', 'o'}


# -------------------------------
# Empty Set
# -------------------------------

empty_set = set()

print(type(empty_set))

# Output:
# <class 'set'>


# -------------------------------
# Adding Elements
# -------------------------------

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)

# Output:
# {1, 2, 3, 4}


# -------------------------------
# Adding Multiple Elements
# -------------------------------

numbers.update([5, 6, 7])

print(numbers)

# Output:
# {1, 2, 3, 4, 5, 6, 7}


# -------------------------------
# Removing Elements
# -------------------------------

numbers.remove(7)

print(numbers)

# Output:
# {1, 2, 3, 4, 5, 6}


# -------------------------------
# discard()
# -------------------------------

numbers.discard(10)

print(numbers)

# Output:
# {1, 2, 3, 4, 5, 6}


# -------------------------------
# pop()
# -------------------------------
# this is not relaible as no indexes are there
temp = {100, 200, 300}

removed = temp.pop()

print("Removed Element :", removed)
print("Remaining Set :", temp)

# Output:
# Removed Element : 100
# Remaining Set : {200, 300}

# Note:
# pop() removes random element,


# -------------------------------
# clear()
# -------------------------------

demo = {1, 2, 3}

demo.clear()

print(demo)

# Output:
# set()


# -------------------------------
# Membership Checking
# -------------------------------

check_set = {10, 20, 30}

print(20 in check_set)
print(50 in check_set)

# Output:
# True
# False


# -------------------------------
# Set Operations
# -------------------------------

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}


# Union

print(x | y)

# Output:
# {1, 2, 3, 4, 5, 6}


# Intersection

print(x & y)

# Output:
# {3, 4}


# Difference

print(x - y)

# Output:
# {1, 2}


# Symmetric Difference

print(x ^ y)

# Output:
# {1, 2, 5, 6}


# -------------------------------
# Subset and Superset
# -------------------------------

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
print(b.issuperset(a))

# Output:
# True
# True


# -------------------------------
# Disjoint Sets
# -------------------------------

m = {1, 2}
n = {5, 6}

print(m.isdisjoint(n))

# Output:
# True


# -------------------------------
# Real Life Use of Set
# -------------------------------

# Removing duplicates from list

marks = [90, 80, 90, 70, 80, 60]

unique_marks = set(marks)

print(unique_marks)

# Output:
# {80, 90, 60, 70}


# Finding common elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print(common)

# Output:
# {3, 4}


# -------------------------------
# Conclusion
# -------------------------------

print("Set is useful for storing unique values.")

# Output:
# Set is useful for storing unique values.