matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[90, 80, 70],
           [6, 5, 4],
           [3, 2, 1]]

resultMatrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

for i in range(len(matrix1)):
    #print(i)
    for j in range(len(matrix1[0])):
            print(matrix1[i][j])
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

#print(resultMatrix)

for add in resultMatrix:
      print(add)