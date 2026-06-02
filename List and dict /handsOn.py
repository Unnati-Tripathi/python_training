"""
LIST COMPREHENSION & DICTIONARY COMPREHENSION
"""

print("=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# ---------------------------------------------
# Example 1: Squares
# ---------------------------------------------

nums = [1, 2, 3, 4, 5]

squares = [x * x for x in nums]

print("\nSquares:")
print(squares)

# ---------------------------------------------
# Example 2: Cubes
# ---------------------------------------------

cubes = [x ** 3 for x in nums]

print("\nCubes:")
print(cubes)

# ---------------------------------------------
# Example 3: Even Numbers
# ---------------------------------------------

even = [x for x in range(20) if x % 2 == 0]

print("\nEven Numbers:")
print(even)

# ---------------------------------------------
# Example 4: Odd Numbers
# ---------------------------------------------

odd = [x for x in range(20) if x % 2 != 0]

print("\nOdd Numbers:")
print(odd)

# ---------------------------------------------
# Example 5: Uppercase Names
# ---------------------------------------------

names = ["amit", "ravi", "neha"]

upper_names = [name.upper() for name in names]

print("\nUppercase Names:")
print(upper_names)

# ---------------------------------------------
# Example 6: Length of Each Word
# ---------------------------------------------

words = ["python", "java", "javascript"]

lengths = [len(word) for word in words]

print("\nWord Lengths:")
print(lengths)

# ---------------------------------------------
# Example 7: Even/Odd Labeling
# ---------------------------------------------

labels = ["Even" if x % 2 == 0 else "Odd"
          for x in range(10)]

print("\nEven/Odd Labels:")
print(labels)

# ---------------------------------------------
# Example 8: Reverse Strings
# ---------------------------------------------

words = ["python", "java", "cpp"]

reversed_words = [word[::-1] for word in words]

print("\nReversed Words:")
print(reversed_words)

# ---------------------------------------------
# Example 9: Flatten Nested List
# ---------------------------------------------

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [num
        for row in matrix
        for num in row]

print("\nFlatten Matrix:")
print(flat)

# ---------------------------------------------
# Example 10: First Letter of Each Name
# ---------------------------------------------

names = ["Amit", "Ravi", "Neha", "Karan"]

first_letters = [name[0] for name in names]

print("\nFirst Letters:")
print(first_letters)


# DICTONARY 


print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION")
print("=" * 50)


# ---------------------------------------------
# Example 11: Number -> Square
# ---------------------------------------------

square_dict = {
    x: x * x
    for x in range(1, 6)
}

print("\nSquare Dictionary:")
print(square_dict)

# ---------------------------------------------
# Example 12: Number -> Cube
# ---------------------------------------------

cube_dict = {
    x: x ** 3
    for x in range(1, 6)
}

print("\nCube Dictionary:")
print(cube_dict)

# ---------------------------------------------
# Example 13: Even Numbers Only
# ---------------------------------------------
#putting condition..
even_square = {
    x: x * x
    for x in range(10)
    if x % 2 == 0
}

print("\nEven Squares:")
print(even_square)

# ---------------------------------------------
# Example 14: Name -> Length
# ---------------------------------------------

names = ["Amit", "Ravi", "Neha"]

name_length = {
    name: len(name)
    for name in names
}

print("\nName Length Dictionary:")
print(name_length)

# ---------------------------------------------
# Example 15: Name -> Uppercase
# ---------------------------------------------

name_upper = {
    name: name.upper()
    for name in names
}

print("\nName -> Uppercase:")
print(name_upper)

# ---------------------------------------------
# Example 16: Reverse Dictionary
# ---------------------------------------------

student = {
    "Amit": 85,
    "Ravi": 90,
    "Neha": 95
}

reverse = {
    value: key
    for key, value in student.items()
}

print("\nReverse Dictionary:")
print(reverse)


# ---------------------------------------------
# Example 18: Multiplication Table of 5
# ---------------------------------------------

table = {
    x: 5 * x
    for x in range(1, 11)
}

print("\nTable of 5:")
print(table)

