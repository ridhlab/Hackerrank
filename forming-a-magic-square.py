def difference(a, matrix):
    difference = 0
    for i in range(9):
        difference += abs(a[i]-matrix[i])
    return difference
    
def formingMagicSquare(matrix)    :
    resultMatrix = [[4,9,2,3,5,7,8,1,6],
                    [8,3,4,1,5,9,6,7,2],
                    [6,1,8,7,5,3,2,9,4],
                    [2,7,6,9,5,1,4,3,8],
                    [4,3,8,9,5,1,2,7,6],
                    [2,9,4,7,5,3,6,1,8],
                    [6,7,2,1,5,9,8,3,4],
                    [8,1,6,3,5,7,4,9,2],]
    matrix0 = []
    for i in range(3):
        for j in range(3):
            matrix0.append(matrix[i][j])
    listDifference = []
    for record in resultMatrix:
        dif = difference(record, matrix0)
        listDifference.append(dif)
    listDifference.sort()
    return listDifference[0]
    
if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    print(result)
    
    