python_students = {"Rahul", "Amit", "Sneha", "John"}
sql_students = {"John", "Sneha", "David", "Meena"}
aws_students = {"Rahul", "David", "Kiran"}

# Students in both Python and SQL
common = python_students & sql_students
print(common)
# {'John', 'Sneha'}


# Students in all 3 courses
allThree = python_students & sql_students & aws_students
print(allThree)
# set()


# Students only in Python
onlyPython = python_students - (sql_students | aws_students)
print(onlyPython)
# {'Amit'}


# Total unique students
totalUnique = python_students | sql_students | aws_students
print(totalUnique)
# {'Rahul', 'Amit', 'Sneha', 'John', 'David', 'Meena', 'Kiran'}


# Students not enrolled in AWS
notAWS = totalUnique - aws_students
print(notAWS)
# {'Amit', 'Sneha', 'John', 'Meena'}



# # Students in more than 1 course
# moreThanOne = ((python_students & sql_students)| (python_students & aws_students)| (sql_students & aws_students))

# print(moreThanOne)
# # {'Rahul', 'Sneha', 'John', 'David'}



# Students in more than 2 courses. 
totalAll = (python_students & sql_students & aws_students) # finding commmon students in all three 
print(totalAll)


# Students whose name starts with 'Ra'
for i in totalUnique:
    if i.startswith("Ra"):
        print(i)

# Rahul
# or we can do it with index 0->R , 1->a , -1->last character , -2-> second character..


# Students whose name ends with 'na' or 'an'
for i in totalUnique:
    if i.endswith("na") or i.endswith("an"):
        print(i)

# Meena