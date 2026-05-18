nums = [1 , 33 , 56 , 1001 , 768]

# Add 89 to the end of the list.
nums.append(89)
print(nums)
# [1, 33, 56, 1001, 768, 89]

# Add 39 to the beginning of the list.
nums.insert(0, 39)
print(nums)
# [39, 1, 33, 56, 1001, 768, 89]

# Add elements of another list [77,66,44] into the existing list.
anotherList = [77 , 66 , 44]
nums += anotherList
print(nums)
# [39, 1, 33, 56, 1001, 768, 89, 77, 66, 44]

# Add [99,88] as a single nested element inside the list.
nums.append([99 , 88])
print(nums)
# [39, 1, 33, 56, 1001, 768, 89, 77, 66, 44, [99, 88]]

# Insert 'Apple' at position 2.
nums.insert(2, 'Apple')
print(nums)
# [39, 1, 'Apple', 33, 56, 1001, 768, 89, 77, 66, 44, [99, 88]]

# Replace 'Apple' with 'Pineapple'.
nums[2] = 'Pineapple'
print(nums)
# [39, 1, 'Pineapple', 33, 56, 1001, 768, 89, 77, 66, 44, [99, 88]]

# Remove the element present at position 4.
nums.pop(4)
print(nums)
# [39, 1, 'Pineapple', 33, 1001, 768, 89, 77, 66, 44, [99, 88]]

# Remove 'Pineapple' from the list.
nums.remove('Pineapple')
print(nums)
# [39, 1, 33, 1001, 768, 89, 77, 66, 44, [99, 88]]