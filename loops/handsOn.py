# while loop
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
# 1
# 2
# 4
# 5
    
    
# for loop
for i in range(1, 6):
    print(i)
# 1
# 2
# 3
# 4
# 5

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# mango
    
    
name = "Unnati"
for ch in name:
    print(ch)
    
# U
# n
# n
# a
# t
# i

for i in range(1, 6):
    if i == 4:
        break
    print(i)
    
    
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
    
    
    # nested loop
    
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
        
        
# enumerate loop

names = ["Aman", "Riya", "Unnati"]

for index, value in enumerate(names):
    print(index, value)
    
    
    
# Dictionary Loop

student = {
    "name": "Unnati",
    "age": 21
}
for key, value in student.items():
    print(key, value)