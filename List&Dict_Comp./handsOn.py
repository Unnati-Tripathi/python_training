# """
# ====================================================
# LIST COMPREHENSION & DICTIONARY COMPREHENSION PRACTICE
# ====================================================

# """

# print("LIST COMPREHENSION PRACTICE")

# # Example 1: Basic List Comprehension

# numbers = [1, 2, 3, 4, 5]

# squares = [num ** 2 for num in numbers]

# print("\nSquares:")
# print(squares)

# # Example 2: Even Numbers

# evens = [num for num in numbers if num % 2 == 0]

# print("\nEven Numbers:")
# print(evens)

# # Example 3: Odd Numbers

# odds = [num for num in numbers if num % 2 != 0]

# print("\nOdd Numbers:")
# print(odds)


# # Example 4: Convert to Uppercase

# names = ["unnati", "amit", "rahul"]

# upper_names = [name.upper() for name in names]

# print("\nUppercase Names:")
# print(upper_names)

# # Example 5: Length of Each Word

# words = ["python", "java", "cpp", "javascript"]

# lengths = [len(word) for word in words]

# print("\nLengths:")
# print(lengths)

# # Example 6: Conditional Expression

# result = ["Even" if num % 2 == 0 else "Odd"
#           for num in range(1, 11)]

# print("\nEven/Odd Labels:")
# print(result)

# # Example 7: Nested Loop

# pairs = [(x, y)
#          for x in range(1, 4)
#          for y in range(1, 4)]

# print("\nPairs:")
# print(pairs)

# # HANDS-ON QUESTIONS (LIST COMPREHENSION)

# print("\n" + "="*50)
# print("LIST COMPREHENSION ASSIGNMENTS")
# print("="*50)

print("\n TODO \n")
# Q1
nums = [10, 20, 30, 40, 50]

# Create a list containing double values

answer = [arr*2   for arr in nums]
print("\n answer1 " , answer)


# Q2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# TODO:
# Create list of numbers divisible by 3

answer = [arr for arr in nums if arr%3==0]
print("\n answer2 " , answer)


# Q3
names = ["ram", "shyam", "gita", "sita"]

# TODO:
# Convert all names into Capitalized format

answer = [num.upper() for num in names]
print("\n answer3 " , answer)



# Q4
nums = [1, 2, 3, 4, 5]

# TODO:
# Create cubes

answer = [ans ** 3 for ans in nums]
print("\n answer4 " , answer)

print("\n")


# DICTIONARY COMPREHENSION

print("DICTIONARY COMPREHENSION PRACTICE")

# Example 1

square_dict = {num: num**2 for num in range(1, 6)}

print("\nSquares Dictionary:")
print(square_dict)

# Example 2

students = ["Amit", "Sara", "Ravi"]

length_dict = {
    name: len(name)
    for name in students
}

print("\nName Length Dictionary:")
print(length_dict)

# Example 3

nums = [1, 2, 3, 4, 5]

even_odd = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in nums
}

print("\nEven Odd Dictionary:")
print(even_odd)

# Example 4

prices = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500
}

discounted = {
    item: price * 0.9
    for item, price in prices.items()
}

print("\nDiscounted Prices:")
print(discounted)

# HANDS-ON QUESTIONS (DICTIONARY COMPREHENSION)

print("\n" + "="*50)
print("DICTIONARY COMPREHENSION ASSIGNMENTS")
print("="*50)
