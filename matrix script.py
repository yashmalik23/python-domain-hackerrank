import re
n, m = map(int,input().split())
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)
s=str()
k=0
for i in range(len(matrix[k])):
    for j in range(n):
        s=s+str(matrix[j][i])
    k+=1
s=re.sub('(?<=\w)([^\w]+)(?=\w)',' ',s)
print(s)