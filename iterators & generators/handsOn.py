"""
===========================================================
PYTHON ITERATORS AND GENERATORS - FULL HANDS-ON PRACTICE
===========================================================

Topics covered:
1. Iterable vs Iterator
2. iter() and next()
3. StopIteration
4. for loop internal working
5. Custom Iterator using class
6. Generator functions using yield
7. yield vs return
8. Generator expressions
9. Memory efficiency
10. Real-world examples
11. Practice questions
12. Interview questions

How to use:
- Run this file section by section.
- Read comments carefully.
- Predict output before running.
- Complete TODO tasks yourself.
===========================================================
"""


# =========================================================
# 1. ITERABLE
# =========================================================

"""
Iterable:
An object that can be looped over.

Examples:
- list
- tuple
- string
- dictionary
- set
- range

If something can be used in a for loop, it is usually iterable.
"""

print("\n" + "=" * 70)
print("1. ITERABLE")
print("=" * 70)

numbers = [10, 20, 30]

for num in numbers:
    print(num)

name = "Python"

for ch in name:
    print(ch)


# =========================================================
# 2. ITERATOR
# =========================================================

"""
Iterator:
An object that gives values one by one using next().

To create an iterator from an iterable, use iter().
"""

print("\n" + "=" * 70)
print("2. ITERATOR")
print("=" * 70)

numbers = [10, 20, 30]

iterator_obj = iter(numbers)

print(next(iterator_obj))   # 10
print(next(iterator_obj))   # 20
print(next(iterator_obj))   # 30

# If we call next() again, it will raise StopIteration.
# Uncomment to see error:
# print(next(iterator_obj))


# =========================================================
# 3. ITERABLE VS ITERATOR
# =========================================================

"""
Iterable:
- Can be passed to iter()
- Example: list, string, tuple

Iterator:
- Can be passed to next()
- Remembers current position
- Gets exhausted after use
"""

print("\n" + "=" * 70)
print("3. ITERABLE VS ITERATOR")
print("=" * 70)

nums = [1, 2, 3]

print("List is iterable:", hasattr(nums, "__iter__"))
print("List is iterator:", hasattr(nums, "__next__"))

it = iter(nums)

print("Iterator has __iter__:", hasattr(it, "__iter__"))
print("Iterator has __next__:", hasattr(it, "__next__"))


# =========================================================
# 4. STOPITERATION
# =========================================================

"""
StopIteration:
Raised when an iterator has no more values.

for loop handles StopIteration automatically.
"""

print("\n" + "=" * 70)
print("4. STOPITERATION")
print("=" * 70)

nums = [100, 200]

it = iter(nums)

print(next(it))
print(next(it))

try:
    print(next(it))

except StopIteration:
    print("No more values left in iterator")


# =========================================================
# 5. HOW FOR LOOP WORKS INTERNALLY
# =========================================================

"""
This:

for x in nums:
    print(x)

Internally works like this:

iterator = iter(nums)

while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break
"""

print("\n" + "=" * 70)
print("5. FOR LOOP INTERNAL WORKING")
print("=" * 70)

nums = [5, 10, 15]

iterator = iter(nums)

while True:
    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break


# =========================================================
# 6. ITERATOR GETS EXHAUSTED
# =========================================================

"""
Once an iterator is consumed, it becomes empty.
"""

print("\n" + "=" * 70)
print("6. ITERATOR GETS EXHAUSTED")
print("=" * 70)

nums = [1, 2, 3]

it = iter(nums)

print(list(it))   # [1, 2, 3]
print(list(it))   # [] because iterator is already exhausted


# =========================================================
# 7. CUSTOM ITERATOR USING CLASS
# =========================================================

"""
To create a custom iterator, define:

1. __iter__()
2. __next__()

__iter__() returns the iterator object.
__next__() returns the next value.
"""

print("\n" + "=" * 70)
print("7. CUSTOM ITERATOR USING CLASS")
print("=" * 70)


class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = CountUpTo(5)

for num in counter:
    print(num)


# =========================================================
# 8. CUSTOM ITERATOR: EVEN NUMBERS
# =========================================================

print("\n" + "=" * 70)
print("8. CUSTOM ITERATOR: EVEN NUMBERS")
print("=" * 70)


class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 2
            return value

        raise StopIteration


evens = EvenNumbers(10)

for num in evens:
    print(num)


# =========================================================
# 9. GENERATOR FUNCTION
# =========================================================

"""
Generator:
A simpler way to create an iterator.

A function becomes a generator function when it uses yield.

yield:
- returns a value
- pauses the function
- remembers where it left off
- resumes from there on next call
"""

print("\n" + "=" * 70)
print("9. GENERATOR FUNCTION")
print("=" * 70)


def count_up_to(limit):
    current = 1

    while current <= limit:
        yield current
        current += 1


gen = count_up_to(5)

print(next(gen))
print(next(gen))
print(next(gen))

print("Using loop:")

for num in gen:
    print(num)


# =========================================================
# 10. YIELD VS RETURN
# =========================================================

"""
return:
- sends one final value
- ends the function

yield:
- sends a value
- pauses the function
- function can continue later
"""

print("\n" + "=" * 70)
print("10. YIELD VS RETURN")
print("=" * 70)


def normal_function():
    return 10
    return 20


print("Normal function:", normal_function())


def generator_function():
    yield 10
    yield 20
    yield 30


g = generator_function()

print(next(g))
print(next(g))
print(next(g))


# =========================================================
# 11. GENERATOR FOR EVEN NUMBERS
# =========================================================

print("\n" + "=" * 70)
print("11. GENERATOR FOR EVEN NUMBERS")
print("=" * 70)


def even_numbers(limit):
    num = 2

    while num <= limit:
        yield num
        num += 2


for even in even_numbers(10):
    print(even)


# =========================================================
# 12. GENERATOR EXPRESSION
# =========================================================

"""
Generator expression:
Similar to list comprehension, but uses () instead of [].

List comprehension creates full list in memory.
Generator expression produces values one by one.
"""

print("\n" + "=" * 70)
print("12. GENERATOR EXPRESSION")
print("=" * 70)

list_comp = [x * x for x in range(1, 6)]
gen_exp = (x * x for x in range(1, 6))

print("List comprehension:", list_comp)
print("Generator expression:", gen_exp)

print(next(gen_exp))
print(next(gen_exp))

print("Remaining values:")

for val in gen_exp:
    print(val)


# =========================================================
# 13. MEMORY EFFICIENCY
# =========================================================

"""
Generators are memory efficient because they do not store all values at once.

They are useful for:
- large files
- logs
- database rows
- API streams
- large numeric sequences
"""

print("\n" + "=" * 70)
print("13. MEMORY EFFICIENCY")
print("=" * 70)


def large_numbers():
    for i in range(1, 6):
        print("Generating:", i)
        yield i


g = large_numbers()

print("Generator created. No values generated yet.")

print(next(g))
print(next(g))

print("Now loop over remaining values:")

for value in g:
    print(value)


# =========================================================
# 14. REAL-WORLD EXAMPLE: READ FILE LINE BY LINE
# =========================================================

"""
Generators are useful for reading large files line by line.

Instead of loading the entire file into memory, we yield one line at a time.
"""

print("\n" + "=" * 70)
print("14. REAL-WORLD EXAMPLE: READ FILE LINE BY LINE")
print("=" * 70)


def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


with open("sample_log.txt", "w") as file:
    file.write("INFO User logged in\n")
    file.write("ERROR Database failed\n")
    file.write("INFO User logged out\n")

for line in read_lines("sample_log.txt"):
    print(line)


# =========================================================
# 15. REAL-WORLD EXAMPLE: FILTER LOG ERRORS
# =========================================================

print("\n" + "=" * 70)
print("15. REAL-WORLD EXAMPLE: FILTER LOG ERRORS")
print("=" * 70)


def error_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                yield line.strip()


for error in error_lines("sample_log.txt"):
    print(error)


# =========================================================
# 16. CHAINING GENERATORS
# =========================================================

"""
You can pass one generator output into another generator.
This is useful in data pipelines.
"""

print("\n" + "=" * 70)
print("16. CHAINING GENERATORS")
print("=" * 70)


def generate_numbers(limit):
    for i in range(1, limit + 1):
        yield i


def square_numbers(numbers):
    for num in numbers:
        yield num * num


nums = generate_numbers(5)
squares = square_numbers(nums)

for square in squares:
    print(square)


# =========================================================
# 17. INFINITE GENERATOR
# =========================================================

"""
Generators can be infinite because they produce one value at a time.

Be careful:
Never directly convert an infinite generator to list.
"""

print("\n" + "=" * 70)
print("17. INFINITE GENERATOR")
print("=" * 70)


def infinite_count():
    num = 1

    while True:
        yield num
        num += 1


counter = infinite_count()

print(next(counter))
print(next(counter))
print(next(counter))


# =========================================================
# 18. PRACTICE QUESTIONS - ITERATORS
# =========================================================

print("\n" + "=" * 70)
print("18. PRACTICE QUESTIONS - ITERATORS")
print("=" * 70)

"""
TODO 1:
Create an iterator from list [10, 20, 30, 40].
Print values using next().
Handle StopIteration safely.
"""

# Write your code here


"""
TODO 2:
Create a custom iterator class ReverseString.

Input:
ReverseString("Python")

Output:
n
o
h
t
y
P
"""

# Write your code here


"""
TODO 3:
Create a custom iterator class SquareNumbers.

Input:
SquareNumbers(5)

Output:
1
4
9
16
25
"""

# Write your code here


# =========================================================
# 19. PRACTICE QUESTIONS - GENERATORS
# =========================================================

print("\n" + "=" * 70)
print("19. PRACTICE QUESTIONS - GENERATORS")
print("=" * 70)

"""
TODO 4:
Create a generator that yields numbers from 1 to n.
"""

# Write your code here


"""
TODO 5:
Create a generator that yields only odd numbers up to n.
"""

# Write your code here


"""
TODO 6:
Create a generator that yields Fibonacci numbers up to n terms.

Example:
fibonacci(6)

Output:
0
1
1
2
3
5
"""

# Write your code here


"""
TODO 7:
Create a generator that reads a file and yields only lines containing "ERROR".
"""

# Write your code here


"""
TODO 8:
Create a generator expression for squares of even numbers from 1 to 20.
"""

# Write your code here


# =========================================================
# 20. INTERVIEW QUESTIONS
# =========================================================

print("\n" + "=" * 70)
print("20. INTERVIEW QUESTIONS")
print("=" * 70)

interview_questions = [
    "1. What is an iterable?",
    "2. What is an iterator?",
    "3. Difference between iterable and iterator?",
    "4. What does iter() do?",
    "5. What does next() do?",
    "6. What is StopIteration?",
    "7. How does a for loop work internally?",
    "8. What are __iter__() and __next__()?",
    "9. What is a generator?",
    "10. What is yield?",
    "11. Difference between yield and return?",
    "12. Difference between list comprehension and generator expression?",
    "13. Why are generators memory efficient?",
    "14. Can a generator be reused after exhaustion?",
    "15. What happens if next() is called after generator is exhausted?",
    "16. Real-world use cases of generators?",
    "17. Difference between range and generator?",
    "18. Can generators be infinite?",
    "19. What is lazy evaluation?",
    "20. Why are generators useful for large files?"
]

for question in interview_questions:
    print(question)


# =========================================================
# 21. QUICK REVISION SUMMARY
# =========================================================

print("\n" + "=" * 70)
print("21. QUICK REVISION SUMMARY")
print("=" * 70)

summary = """
ITERABLE:
Can be looped over.
Example: list, tuple, string, dict, set, range.

ITERATOR:
Object that gives next value using next().
Has __iter__() and __next__().

iter():
Converts iterable into iterator.

next():
Gets next value from iterator.

StopIteration:
Exception raised when iterator is exhausted.

GENERATOR:
A special iterator created using yield.

yield:
Returns a value and pauses function.

return:
Returns value and ends function.

GENERATOR EXPRESSION:
Like list comprehension but lazy and memory efficient.

Example:
(x*x for x in range(10))

Main benefit:
Generators save memory because they produce values one by one.
"""

print(summary)

print("\nPractice file completed. Now solve all TODO tasks yourself!")