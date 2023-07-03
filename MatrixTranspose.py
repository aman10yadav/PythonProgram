matrix1 = [[1, 2],
           [3, 4],
           [5, 6]]

resultMatrix = [[0, 0, 0],
                [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        resultMatrix[j][i] = matrix1[i][j]

for res in resultMatrix:
    print(res)