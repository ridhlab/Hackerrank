def changeElement(r, c, arr):
    suMM = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] +arr[r+2][c+2]
    return suMM
def hourglassSum(arr):
    listResult = [[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
    for row in range(4):
        for column in range(4):
            listResult[row][column] = changeElement(row, column, arr)
    LisTTT = []
    for i in range (4):
        for j in range(4):
            LisTTT.append(listResult[i][j])
    LisTTT.sort(reverse=True)
    return LisTTT[0]

if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #arr = [[1,1,1,0,0,0],
    #      [0,1,0,0,0,0],
    #      [1,1,1,0,0,0],
    #      [0,0,2,4,4,0],
    #      [0,0,0,2,0,0],
    #      [0,0,1,2,4,0]]
    result = hourglassSum(arr)
    print(result)
