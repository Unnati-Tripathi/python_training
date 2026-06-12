# Assignment on Reg exp

# 1. Extract Email Addresses
# Given a paragraph of text, extract all valid email addresses.
# Example:
# text = "Contact us at support@test.com or admin123@gmail.com"
# Output:
# ['support@test.com', 'admin123@gmail.com']

import re



text = "Contact us at support@test.com or admin123@gmail.com"
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(emails)

# Symbol	Meaning	
# +	        1 or more	
# *	        0 or more
# ?	        0 or 1	
# {3}	    exactly 3	
# {2,5} 	2 to 5	
# {2,}	    at least 2	


# 2. Validate Password
# Write a regex to validate a password that must:
# Be at least 8 characters
# Contain at least 1 uppercase letter
# Contain at least 1 lowercase letter
# Contain at least 1 digit
# Contain at least 1 special character
# Examples:
# Password@123  # Valid
# password123   # Invalid


password = "Password@123" 
check=  re.fullmatch(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}', password)
if check:
    print("Valid")
else:
    print("not Valid")



# ^
# Start of string.
# $
# End of string.


# 3. Extract Dates
# Extract dates from text in formats:
# DD-MM-YYYY
# DD/MM/YYYY
# YYYY-MM-DD
# Example:
# "Meeting on 12-05-2026 and another on 2026-06-01"


text = "Meeting on 12-05-2026 and another on 2026-06-01 and 15/08/2025"
dates = re.findall(
    r'\b(?:\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\b',
    text
)
print(dates)



# \d{2}-\d{2}-\d{4}                    ==digits only of range{2}
# |
# \d{2}/\d{2}/\d{4}
# |                                    ==OR
# \d{4}-\d{2}-\d{2}



# 4. Find Duplicate Words
# Detect consecutive duplicate words.
# Example:
# "This is is a sample sample text."
# Output:
# ['is', 'sample']

text = "This is bis a sample sample is text."
# duplicates = re.findall(r'(\w+)\s+\1', text) 
# # ['is', 'sample']
duplicates = re.findall(r'\b(\w+)\s+\1\b', text)
print(duplicates)



# \s+ means: one or more whitespace characters
# (space)
# (tab)
# (newline)

# (\w+)  -> captures "is"
# \s+    -> matches space
# \1     -> matches "is" again
# \b     ->word boundary



# 5. Convert Multiple Spaces to One
# Replace all occurrences of multiple spaces/tabs with a single space.
# Example:
# "Hello     World\t\tPython"
# Output:
# "Hello World Python"

text = "Hello     World\t\tPython"
result = re.sub(r'\s+', ' ', text)
print(result)



# 6. Log File Parser
# Given log entries:
# 2026-06-01 10:23:45 ERROR Database connection failed
# 2026-06-01 10:24:12 INFO User login successful
# Extract:
# Timestamp
# Log level
# Message
# Return as dictionaries.


logs = """2026-06-01 10:23:45 ERROR Database connection failed
2026-06-01 10:24:12 INFO User login successful"""
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.+)'
result = []
for match in re.findall(pattern, logs):
    result.append({
        "timestamp": match[0],
        "level": match[1],
        "message": match[2]
    })
print(result)

# . => Any character except newline.



# 7. Extract HTML Tags
# Given:
# <div>Hello</div>
# <p>World</p>
# <a href="#">Link</a>Give feedback
# Extract only tag names:
# Output:
# ['div', 'p', 'a']
 

html = """<div>Hello</div>
<p>World</p>
<a href="#">Link</a>"""

tags = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)\b', html)

print(tags)

# * -> 0 or more times ye sequesnce check krlo aage



# 8 Extract Currency Values
# From text:
# "Revenue was $1,200.50, profit ₹50,000 and loss €300"
# Extract:
# ['$1,200.50', '₹50,000', '€300']
 

text = "Revenue was $1,200.50, profit ₹50,000 and loss €300"

currency = re.findall(r'[$₹€]\d{1,3}(?:,\d{3})*(?:\.\d+)?|[$₹€]\d+(?:\.\d+)?', text)

print(currency)