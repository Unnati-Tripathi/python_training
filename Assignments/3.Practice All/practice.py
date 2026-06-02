# TASK

borrow_records = [
    ("Unnati", "Python Basics", "Programming"),
    ("Rahul", "DBMS Made Easy", "Database"),
    ("Priya", "Python Basics", "Programming"),
    ("Aman", "Networking Guide", "Computer Networks"),
    ("Unnati", "Python Basics", "Programming"),
    ("Sagar", "DBMS Made Easy", "Database")
]


# Remove duplicate borrow records.

no_dup = set(borrow_records)

print("After removing duplicates:")
print(no_dup)


# Find all unique book categories.

books = set()

for i in no_dup:
    index = 0

    for j in i:
        if index == 2:
            books.add(j)

        index += 1

print("Unique book categories:")
print(books)


# Create a dictionary where:
# key = student name
# value = list of books borrowed

dict_borrow_record = {}

for i in no_dup:
    index = 0
    user = ""
    book = ""

    for j in i:
        if index == 0:
            user = j

        if index == 1:
            book = j

        index += 1

    if user not in dict_borrow_record:
        dict_borrow_record[user] = []

    dict_borrow_record[user].append(book)

print("\nStudent wise borrowed books:")
print(dict_borrow_record)


# Count how many times each book was borrowed.

freq = {}

for user in dict_borrow_record:
    for book in dict_borrow_record[user]:

        if book not in freq:
            freq[book] = 1

        else:
            freq[book] += 1

print("Book frequency:")
print(freq)


# Find students who borrowed "Python Basics".

python_students = []

for i in no_dup:
    index = 0
    user = ""
    book = ""

    for j in i:
        if index == 0:
            user = j

        if index == 1:
            book = j

        index += 1

    if book == "Python Basics":
        python_students.append(user)

print("Students who borrowed Python Basics:")
print(python_students)


# Store each unique record as a tuple.

unique_tuple = tuple(no_dup)

print("\nUnique records stored as tuple:")
print(unique_tuple)


# Check if "Database" category exists.

print("\nIs Database category exists?")
print("Database" in books)


# Print final summary.

print("\nFinal Summary:")
print("Total records:", len(borrow_records))
print("Total unique records:", len(no_dup))
print("Total unique categories:", len(books))
print("Student wise books:", dict_borrow_record)
print("Book frequency:", freq)