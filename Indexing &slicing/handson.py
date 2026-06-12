"""
============================================================
PYTHON INDEXING, SLICING & REVERSE INDEXING - DEEP HANDS-ON
============================================================
"""


# ============================================================
# 1. WHAT IS INDEXING?
# ============================================================

"""
Indexing means accessing one element from a sequence.

Sequences in Python:
- string
- list
- tuple

Python indexing starts from 0.

Example:

String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5

Negative indexing starts from the end.

String:       P   y   t   h   o   n
Positive:     0   1   2   3   4   5
Negative:    -6  -5  -4  -3  -2  -1
"""

s = "Python"

print("\n========== BASIC INDEXING ==========")

print("String:", s)
print("s[0] =", s[0])      # First character
print("s[1] =", s[1])      # Second character
print("s[2]" , s[2])
print("s[5] =", s[5])      # Last character using positive index
print("s[-1] =", s[-1])    # Last character using negative index
print("s[-2] =", s[-2])    # Second last character


# ============================================================
# 2. POSITIVE INDEXING
# ============================================================

print("\n========== POSITIVE INDEXING ==========")

name = "Unnati"

print("String:", name)

print("Index 0:", name[0])
print("Index 1:", name[1])
print("Index 2:", name[2])
print("Index 3:", name[3])
print("Index 4:", name[4])
print("Index 5:", name[5])


"""
Important:
If you access an index that does not exist, Python gives IndexError.

"""


# ============================================================
# 3. NEGATIVE / REVERSE INDEXING
# ============================================================

print("\n========== NEGATIVE INDEXING ==========")

word = "Computer"

print("String:", word)

print("word[-1] =", word[-1])   # Last character
print("word[-2] =", word[-2])   # Second last
print("word[-3] =", word[-3])
print("word[-4] =", word[-4])
print("word[-5] =", word[-5])
print("word[-6] =", word[-6])
print("word[-7] =", word[-7])
print("word[-8] =", word[-8])   # First character

"""
For a string of length n:

Positive index:
0 to n-1

Negative index:
-n to -1

For word = "Computer", length is 8.

Positive:
C  o  m  p  u  t  e  r
0  1  2  3  4  5  6  7

Negative:
 C   o   m   p   u   t   e   r
-8  -7  -6  -5  -4  -3  -2  -1
"""



# ============================================================
# 5. BASIC SLICING
# ============================================================

"""
Slicing is used to extract a part of a sequence.

Syntax:

sequence[start:end]

Important:
- start is included
- end is excluded

Example:

s = "Python"

s[0:4]

Index:   0 1 2 3 4 5
String:  P y t h o n

s[0:4] means take indexes 0,1,2,3.
So output is "Pyth".
"""

print("\n========== BASIC SLICING ==========")

s = "PythonProgramming"

print("String:", s)

print("s[0:6] =", s[0:6])       # Python
print("s[6:17] =", s[6:17])     # Programming
print("s[:6] =", s[:6])         # From start to index 5
print("s[6:] =", s[6:])         # From index 6 to end
print("s[:] =", s[:])           # Full string copy


# ============================================================
# 7. SLICING WITH NEGATIVE INDEXES
# ============================================================

print("\n========== SLICING WITH NEGATIVE INDEXES ==========")

s = "Programming"

print("String:", s)

print("s[-4:] =", s[-4:])       # Last 4 characters
print("s[:-4] =", s[:-4])       # Everything except last 4
print("s[-7:-3] =", s[-7:-3])  
print("s[2:-2] =", s[2:-2])

"""
For s = "Programming"

Positive:
 P  r  o  g  r  a  m  m  i  n  g
 0  1  2  3  4  5  6  7  8  9  10

Negative:
  P    r    o    g    r    a    m    m    i    n    g
-11  -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
"""


# ============================================================
# 8. SLICING WITH STEP
# ============================================================

"""
Full slicing syntax:

sequence[start:end:step]

step means jump.

s[::2] means:
Start from beginning, go till end, take every 2nd character.

s[1::2] means:
Start from index 1, go till end, take every 2nd character.
"""

print("\n========== SLICING WITH STEP ==========")

s = "ABCDEFGHIJ"

print("String:", s)

print("s[::1] =", s[::1])       # Normal
print("s[::2] =", s[::2])       # Every second character
print("s[::3] =", s[::3])       # Every third character
print("s[1::2] =", s[1::2])     # Every second character from index 1
print("s[2::2] =", s[2::2])     # Every second character from index 2


# ============================================================
# 9. REVERSE STRING USING SLICING
# ============================================================

"""
s[::-1]

Meaning:
- start: not given
- end: not given
- step: -1

When step is negative, Python moves from right to left.

So s[::-1] reverses the sequence.
"""

print("\n========== REVERSING USING SLICING ==========")

s = "Python"

print("String:", s)
print("Reversed:", s[::-1])

print("s[::-2] =", s[::-2])
print("s[::-3] =", s[::-3])



print("\n========== NEGATIVE STEP ==========")

s = "ABCDEFG"

print("String:", s)

print("s[5:1:-1] =", s[5:1:-1])     # FEDC
print("s[6:2:-1] =", s[6:2:-1])     # GFED
print("s[-1:-5:-1] =", s[-1:-5:-1]) # GFED
print("s[3::-1] =", s[3::-1])       # DCBA
print("s[:3:-1] =", s[:3:-1])       # GFE




# ============================================================
# 12. PALINDROME CHECK
# ============================================================

"""
Palindrome means the word is same forward and backward.
"""

print("\n========== PALINDROME CHECK ==========")

word = "madam"

if word == word[::-1]:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")

word = "python"

if word == word[::-1]:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")


# ============================================================
# 13. REVERSE EACH WORD IN A SENTENCE
# ============================================================

print("\n========== REVERSE EACH WORD ==========")

sentence = "I love Python"

words = sentence.split()

reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)

print("Original:", sentence)
print("Each word reversed:", result)


# ============================================================
# 14. REVERSE WORD ORDER
# ============================================================

print("\n========== REVERSE WORD ORDER ==========")

sentence = "I love Python programming"

words = sentence.split()

reversed_sentence = " ".join(words[::-1])

print("Original:", sentence)
print("Word order reversed:", reversed_sentence)



# ============================================================
# 16. LIST INDEXING AND SLICING
# ============================================================

print("\n========== LIST INDEXING AND SLICING ==========")

numbers = [10, 20, 30, 40, 50, 60, 70]

print("List:", numbers)

print("numbers[0] =", numbers[0])
print("numbers[-1] =", numbers[-1])
print("numbers[1:5] =", numbers[1:5])
print("numbers[:3] =", numbers[:3])
print("numbers[3:] =", numbers[3:])
print("numbers[::-1] =", numbers[::-1])
print("numbers[::2] =", numbers[::2])


# ============================================================
# 17. LISTS ARE MUTABLE
# ============================================================

print("\n========== LIST MUTABILITY ==========")

numbers = [10, 20, 30, 40]

print("Before:", numbers)

numbers[0] = 100

print("After changing index 0:", numbers)

numbers[1:3] = [200, 300]

print("After slice update:", numbers)


# ============================================================
# 18. TUPLE INDEXING AND SLICING
# ============================================================

print("\n========== TUPLE INDEXING AND SLICING ==========")

t = (10, 20, 30, 40, 50)

print("Tuple:", t)

print("t[0] =", t[0])
print("t[-1] =", t[-1])
print("t[1:4] =", t[1:4])
print("t[::-1] =", t[::-1])

"""
Tuples support indexing and slicing.
But tuples are immutable, so you cannot update elements.
"""


# ============================================================
# 19. OUT OF RANGE BEHAVIOR
# ============================================================

"""
Important difference:

Indexing out of range gives error.
Slicing out of range does NOT give error.

Example:
s[100]      -> IndexError
s[0:100]    -> Works, returns available characters
"""

print("\n========== OUT OF RANGE BEHAVIOR ==========")

s = "Python"

print("s[0:100] =", s[0:100])
print("s[100:200] =", s[100:200])   # Empty string

# Uncomment to see error:
# print(s[100])


# ============================================================
# 20. TRICKY CASES
# ============================================================

print("\n========== TRICKY CASES ==========")

s = "ABCDEFGHIJ"

print("String:", s)

print("s[2:8] =", s[2:8])
print("s[2:8:2] =", s[2:8:2])
print("s[8:2:-1] =", s[8:2:-1]) #we need to give indexes in right to left sequence in neg. indexes
print("s[-2:-8:-1] =", s[-2:-8:-1])
print("s[-8:-2] =", s[-8:-2])
print("s[-1:-6:-1] =", s[-1:-6:-1])
print("s[5:1:-2] =", s[5:1:-2])
print("s[:5:-1] =", s[:5:-1])
print("s[5::-1] =", s[5::-1])




# ============================================================
#  NESTED LIST SHALLOW COPY WARNING
# ============================================================

print("\n========== SHALLOW COPY WARNING ==========")

a = [[1, 2], [3, 4]]

b = a[:]

b[0][0] = 999

print("a:", a)
print("b:", b)

"""
Because slicing created a new outer list,
but the inner lists are still shared.
"""
