# =========================================================
# 4. PYTHON REGULAR EXPRESSIONS
# =========================================================

"""
Regular Expression, also called regex, is used for pattern matching.

We use the re module.

Common functions:

re.search()    -> finds first match
re.findall()   -> returns all matches
re.match()     -> checks from beginning
re.sub()       -> replaces pattern
re.split()     -> splits using pattern
"""

print("\n" + "=" * 60)
print("4. REGULAR EXPRESSIONS")
print("=" * 60)

import re
#module importing for using reg. exp

# Example 1: search()

text = "My phone number is 9876543210"
match = re.search(r"\d+", text)
if match:
    print("Number found:", match.group())


text = "abc123xyz456"
match = re.search(r"\d+", text)
print(match.group())
print(match)

text = "Hello World"
match = re.search(r"\d+", text)
print(match)

# Output:
# None

# Now if you do:
print(match.group())

# you get:
# AttributeError


# This is the regex pattern.
# r
# Means Raw String.
# \d = Match a digit (0-9)
# search() - returns the first match only.
# .group() extracts only the matched text from the Match object

# Example 2: findall()

text = "My numbers are 9876543210 and 9123456789"
numbers = re.findall(r"\d+", text)
print("All numbers:", numbers)
# returns list

# Example 3: match()

text = "Python is easy"
result = re.match(r"Python", text)
if result:
    print("Text starts with Python")


text = "Is Python is easy..?"
result = re.match(r"Python", text)
if result:
    print("Text starts with Python")


# Example 4: sub()

text = "My number is 9876543210"

hidden = re.sub(r"\d", "*", text)

print("Hidden number:", hidden)

# sub stands for substitute (replace).
# \d+ means: One or more consecutive digits
# The entire number is treated as one match.


# Example 5: split()

text = "apple,banana;orange mango"
fruits = re.split(r"[,;\s]+", text)
print("Fruits:", fruits)


# re.split() allows multiple separators.
# whitespace (\s)

# Example 6: Email validation

email = "unnati@example.com"

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")



# ^ Means:Start of string
# + Means:One or more characters
# $ Means:End of string

# Example 7: Phone number validation

phone = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, phone):
    print("Valid Indian phone number")
else:
    print("Invalid phone number")


# ---------------------------------------------------------
# COMMON REGEX SYMBOLS
# ---------------------------------------------------------

"""
\d   -> digit, 0 to 9
\D   -> non-digit
\w   -> letter, digit, underscore
\W   -> special character
\s   -> space
\S   -> non-space

+    -> one or more
*    -> zero or more
?    -> zero or one
.    -> any character except newline

^    -> starts with
$    -> ends with

[abc]     -> a or b or c
[a-z]     -> lowercase letters
[A-Z]     -> uppercase letters
[0-9]     -> digits
{n}       -> exactly n times
{n,}      -> n or more times
{n,m}     -> between n and m times
"""

