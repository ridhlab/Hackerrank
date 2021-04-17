# Bot Saves Princess
# ==================
# Diberikan sebuah grid persegi
# Dimana ada sebuah ratu yang terjebak di salah satu dari empat sudut grid persegi
# Grid persegi itu berukuran N*N, dimana 3 <= N < 100, dan N bilangan ganjil
# Bot disimbolkan dengan m
# Ratu disimbolkan dengan p
# ========================================
# Contoh
#      ---
#      -m-
#      p--
# =========
# Cari langkah=tercepat supaya bot bisa menyelamatkan ratu

def move_mtop(position_m, position_p):
    praw = position_p[0]
    pcolumn = position_p[1]
    mraw = position_m[0]
    mcolumn = position_m[1]
    while True:
        if mraw == praw:
            if mcolumn > pcolumn:
                n = pcolumn
                if position_m[1] > n:
                    print("LEFT")
                    position_m = [mraw, mcolumn-1]
                    move_mtop(position_m, position_p)
                else:
                    break                    
            else:
                n = pcolumn
                if position_m[1] < n:
                    print("RIGHT")
                    position_m = [mraw, mcolumn+1]
                    move_mtop(position_m, position_p)
                else:
                    break
        elif mraw > praw:
            n = praw
            if position_m[0] > n:
                print("UP")
                position_m = [mraw-1, mcolumn]
                move_mtop(position_m, position_p)
            else:
                break         
        else:
            n = praw 
            if position_m[0] < n:
                print("DOWN")
                position_m = [mraw+1, mcolumn]
                move_mtop(position_m, position_p)
            else:
                break         
        break
        
def check_posp(n, position_m, position_p):
    test = True
    while True:
        if position_p[0] == 0 and position_p[1] == n-1:
            pass
        elif position_p[0] == n-1 and position_p[1] == 0:
            pass
        elif position_p[0] == 0 and position_p[1] == 0:
            pass
        elif position_p[0] == n-1 and position_p[1] == n-1:
            pass
        else:
            test = False
            return "error"
        break
    if test == True:
        move = move_mtop(position_m, position_p)
        return move
    else:
        pass
    
def check_morp(n, grid_ndim):
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
    if test == True:
        check = check_posp(n, position_m, position_p)
        return check
    else:
        pass
        
def displayPathtoPrincess(n, grid):
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
        check = check_morp(n, grid_ndim)
        return check
    else:
        pass
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
a = displayPathtoPrincess(m,grid)
