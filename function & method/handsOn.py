
# =========================================================
# 1. FUNCTIONS IN PYTHON
# =========================================================

"""
A function is a reusable block of code.

Syntax:

def function_name(parameters):
    code
    return value
"""

print("\n" + "=" * 60)
print("1. FUNCTIONS")
print("=" * 60)


# Example 1: Simple function

def greet():
    print("Hello, welcome to Python!")


greet()


# Example 2: Function with parameter

def greet_user(name):
    print("Hello", name)


greet_user("Unnati")


# Example 3: Function with return

def add(a, b):
    return a + b


result = add(10, 20)
print("Addition:", result)


# Example 4: Function without return

def print_square(num):
    print(num * num)


value = print_square(5)
print("Returned value:", value)  # None


# Example 5: Default parameter

def welcome(name="Guest"):
    print("Welcome", name)


welcome()
welcome("Unnati")
# If the caller does not provide a value, Python uses the default one.

# What happens if the default value is mutable?
# ❌ Dangerous:

def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))
print(add_item(3))

# Output:
# [1]
# [1, 2]
# [1, 2, 3]


# Correct Way
def add_item(item, my_list=None):

    if my_list is None:
        my_list = []

    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))
print(add_item(3))



# Example 6: Keyword arguments

def student_info(name, age, city):
    print(name, age, city)


student_info(age=21, city="Lucknow", name="Unnati")
# not searching by index but by parameters

# Example 7: *args

def total_marks(*marks):
    return sum(marks)


print("Total marks:", total_marks(80, 90, 85))
# The * collects all positional arguments into a tuple.

# Example 8: **kwargs

def show_details(**details):
    print(details)


show_details(name="Unnati", role="Intern", city="Lucknow")
# collects keyword arguments into a dictionary


# =========================================================
# 2. METHODS IN PYTHON
# =========================================================

"""
A method is also a function, but it is attached to an object.

Example:
name.upper()

Here upper() is a string method.
"""

print("\n" + "=" * 60)
print("2. METHODS")
print("=" * 60)


# String methods

name = "  unnati tripathi  "

print("Original:", name)
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Title:", name.title())
print("Strip:", name.strip())
print("Replace:", name.replace("unnati", "Unnati"))
print("Count:", name.count("i"))


# List methods

numbers = [10, 20, 30]

numbers.append(40)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)


# Dictionary methods

student = {
    "name": "Unnati",
    "age": 21,
    "city": "Lucknow"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Get name:", student.get("name"))
print("Get marks:", student.get("marks", "Not Available"))

student.update({"age": 22})
print("After update:", student)

