# Bot Saves Princess 2
# ====================
# Diberikan sebuah grid persegin N*N, N < 100
# Bot disimbolkan dengan m
# Ratu disimbolkan dengan p
# ========================================
# Sample input
# 5 -> N = (grid persegi)
# 2 3 -> posisi dari bot
# -----
# -----
# p--m-
# -----
# -----
# Sample output
# LEFT -> langkah selanjutnya supaya lebih dekat ke ratu

def move_mtop(n, position_m, position_p):
    praw = position_p[0]
    pcolumn = position_p[1]
    mraw = position_m[0]
    mcolumn = position_m[1]
    while True:
        if mraw == praw:
            if mcolumn > pcolumn:
                return "LEFT"
            else:
                return "RIGHT"
        elif mraw > praw:
            return "UP"
        else:
            return "DOWN" 
        break
            
def check_morp(n, grid_ndim, a):
    for i in range(n):
        test = True
        for a in range(n):
            if grid_ndim[i][a] == '-':
                pass
            elif grid_ndim[i][a] == 'm':
                position_m = [i, a]
            elif grid_ndim[i][a] == 'p':
                position_p = [i, a]
            else:
                test = False
                return "error"
                break
        if test == False:
            break
        else:
            pass
    if position_m == a:
        test = False
    else:
        test = True
    if test == True:
        check = move_mtop(n, position_m, position_p)
        return check
    else:
        pass

def nextMove(n,r,c,grid):
    grid_ndim = []
    for i in range(n):
        test = True
        a = list(grid[i])
        grid_ndim.append(a)
        if len(grid_ndim[i]) != n:
            test = False
            return "error"
            break
        else:
            pass
    if test == True:
        position_m =[r,c]
        check = check_morp(n, grid_ndim, position_m)
        return check
    else:
        pass
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))