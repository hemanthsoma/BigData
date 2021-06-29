first = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
second = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
result = [
    [0]*3,
    [0]*3,
    [0]*3
]
for i in range(len(first)):
    for j in range(len(second)):
        result[i][j]=first[i][j]+second[i][j]
for k in result:
    print(k)