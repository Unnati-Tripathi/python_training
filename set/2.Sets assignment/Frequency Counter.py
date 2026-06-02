nums = [1,2,2,3,4,4,4,5]

# finding unique values

unique_nums = set(nums)
print(unique_nums)
# {1, 2, 3, 4, 5}


# finding duplicate values

dup = set()
for x in nums:
    if nums.count(x) > 1:
        dup.add(x)

print(dup)
# {2, 4}
#we can do it in different way as well if  it is not in unique then push it into another set and print that..



# finding frequency of each element

# Frequency of each value 

for val in unique_nums:
    total = nums.count(val)
    print(val , "comes" , total , "times")

print()
# 1 comes 1 times
# 2 comes 2 times
# 3 comes 1 times
# 4 comes 3 times
# 5 comes 1 times