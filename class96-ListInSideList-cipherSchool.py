# List inside List
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 3 items ---> 3 List
print(matrix[2])

for i in matrix:
    for j in i:

        print(j,end=" ")

print(matrix[2][0])

s = "string"
print(type(s))
