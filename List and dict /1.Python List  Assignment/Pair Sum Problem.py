# list = [1,2,3,4,5,6,7,8]
# z = 9
# Find all pairs of elements whose sum is equal to z.


list = [1,2,3,4,5,6,7,8]
z=9
answer = []

for i in range(0 , len(list)):
    for j in range(i+1 , len(list)):
        if(list[i] + list[j] == z):
            answer.append((list[i] , list[j]))
    
answer = tuple(answer)
print(answer)