matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix.reverse()

l = len(matrix)
a=[]
for i in range(l-1, -1, -1):
    temp=[]
    for j in range(l-1, -1, -1):
        temp.append(matrix[j][i])
    a.append(temp)
    # print(temp)
    # print(a)
        
print(a)