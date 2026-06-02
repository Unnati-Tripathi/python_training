# Create dictionary:
# students = {
#     "Rahul": 85,
#     "Sneha": 67,
#     "Amit": 67,
#     "John": 45
# }
# Tasks:
# Find topper
# Find failed students (<50)
# Find students with same marks
# Print grades



students = {
    "Rahul": 85,
    "Sneha": 67,
    "Amit": 67,
    "John": 45
}
 
 # Find topper
maxi=0
for key , val in students.items():
    maxi =max(maxi , val)

ans=""
for key , val in students.items():
    if(val==maxi):
        ans = key

print(ans)




# Find failed students (<50)
failed = list()
for std , mark in students.items():
    if(mark<50):
        failed.append(std)

print(failed)







# Find students with same marks
same_marks = {}

for std, mark in students.items():

    if mark not in same_marks:
        same_marks[mark] = []

    same_marks[mark].append(std)

print(same_marks)

# Output:
# {
#   85: ['Rahul'],
#   67: ['Sneha', 'Amit'],
#   45: ['John']
# }





# Print grades
grades = list()
for mark in students.values():
    grades.append(mark)

print(grades)